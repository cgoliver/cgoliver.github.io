#!/usr/bin/env python3
"""
encrypt_baby.py — build script for the encrypted personal wiki at baby.html.

reads markdown files from _baby_src/, encrypts the bundle with AES-GCM using a
password-derived key (PBKDF2-HMAC-SHA256, 600k iterations), and embeds the
ciphertext into baby.html between the /*ENC_BEGIN*//*ENC_END*/ sentinels.

usage:
    python3 encrypt_baby.py                # prompts for password
    BABY_PASSWORD=hunter2 python3 encrypt_baby.py
    python3 encrypt_baby.py --verify       # roundtrip check after encrypting

source file format (each *.md in _baby_src/ becomes a page):
    ---
    title: Display Title
    order: 10
    ---
    # heading

    body markdown...

if no front matter is present, the file stem is used as title and order=100.
the page id is derived from the filename stem.
"""
from __future__ import annotations

import argparse
import base64
import getpass
import json
import os
import re
import secrets
import sys
from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ROOT = Path(__file__).resolve().parent
SRC_DIR = ROOT / "_baby_src"
HTML_PATH = ROOT / "baby.html"

PBKDF2_ITER = 600_000
SALT_LEN = 16
IV_LEN = 12
KEY_LEN = 32

BEGIN = "/*ENC_BEGIN*/"
END = "/*ENC_END*/"

FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n(.*)\Z", re.DOTALL)
SENTINEL_RE = re.compile(re.escape(BEGIN) + r".*?" + re.escape(END), re.DOTALL)
ID_RE = re.compile(r"[^a-z0-9]+")


def b64(b: bytes) -> str:
    return base64.b64encode(b).decode("ascii")


def slug(name: str) -> str:
    s = ID_RE.sub("-", name.lower()).strip("-")
    return s or "page"


def parse_front_matter(text: str) -> tuple[dict, str]:
    m = FM_RE.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip().lower()] = v.strip().strip('"').strip("'")
    return meta, m.group(2)


def load_pages() -> list[dict]:
    if not SRC_DIR.exists():
        sys.exit(f"error: {SRC_DIR} does not exist — create it and add .md files")
    files = sorted(SRC_DIR.glob("*.md"))
    if not files:
        sys.exit(f"error: no .md files in {SRC_DIR}")
    pages: list[dict] = []
    seen_ids: set[str] = set()
    for f in files:
        meta, body = parse_front_matter(f.read_text(encoding="utf-8"))
        page_id = meta.get("id") or slug(f.stem)
        if page_id in seen_ids:
            sys.exit(f"error: duplicate page id {page_id!r} (file {f.name})")
        seen_ids.add(page_id)
        title = meta.get("title") or f.stem.replace("_", " ").replace("-", " ").strip()
        category = meta.get("category") or None
        try:
            order = int(meta.get("order", "100"))
        except ValueError:
            order = 100
        page = {
            "id": page_id,
            "title": title,
            "order": order,
            "content": body.strip("\n"),
        }
        if category:
            page["category"] = category
        pages.append(page)
    pages.sort(key=lambda p: (p["order"], p["title"].lower()))
    for p in pages:
        del p["order"]
    return pages


def derive_key(password: str, salt: bytes) -> bytes:
    return PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LEN,
        salt=salt,
        iterations=PBKDF2_ITER,
    ).derive(password.encode("utf-8"))


def encrypt(password: str, pages: list[dict]) -> dict:
    plaintext = json.dumps({"v": 1, "pages": pages}, ensure_ascii=False).encode("utf-8")
    salt = secrets.token_bytes(SALT_LEN)
    iv = secrets.token_bytes(IV_LEN)
    key = derive_key(password, salt)
    ct = AESGCM(key).encrypt(iv, plaintext, None)
    return {
        "v": 1,
        "kdf": "PBKDF2",
        "hash": "SHA-256",
        "iter": PBKDF2_ITER,
        "salt": b64(salt),
        "iv": b64(iv),
        "ct": b64(ct),
    }


def decrypt_roundtrip(password: str, blob: dict) -> dict:
    key = derive_key(password, base64.b64decode(blob["salt"]))
    pt = AESGCM(key).decrypt(
        base64.b64decode(blob["iv"]),
        base64.b64decode(blob["ct"]),
        None,
    )
    return json.loads(pt.decode("utf-8"))


def embed(blob_json: str) -> None:
    if not HTML_PATH.exists():
        sys.exit(f"error: {HTML_PATH} not found")
    html = HTML_PATH.read_text(encoding="utf-8")
    if not SENTINEL_RE.search(html):
        sys.exit(f"error: sentinels {BEGIN}/{END} not found in baby.html")
    new_html = SENTINEL_RE.sub(BEGIN + blob_json + END, html, count=1)
    HTML_PATH.write_text(new_html, encoding="utf-8")


def get_password(args: argparse.Namespace) -> str:
    pw = os.environ.get("BABY_PASSWORD")
    if pw:
        return pw
    pw = getpass.getpass("password: ")
    if not args.no_confirm:
        if getpass.getpass("confirm:  ") != pw:
            sys.exit("error: passwords do not match")
    if len(pw) < 8:
        sys.exit("error: password must be at least 8 characters")
    return pw


def main() -> None:
    ap = argparse.ArgumentParser(description="encrypt baby wiki source into baby.html")
    ap.add_argument("--verify", action="store_true", help="decrypt and check roundtrip after embedding")
    ap.add_argument("--no-confirm", action="store_true", help="do not prompt to confirm password")
    ap.add_argument("--reset", action="store_true", help="reset baby.html to placeholder (no content) and exit")
    args = ap.parse_args()

    if args.reset:
        embed('{"v":1,"placeholder":true}')
        print("reset baby.html to placeholder")
        return

    password = get_password(args)
    pages = load_pages()
    pt_size = len(json.dumps({"v": 1, "pages": pages}, ensure_ascii=False).encode("utf-8"))
    blob = encrypt(password, pages)
    blob_json = json.dumps(blob, separators=(",", ":"))
    embed(blob_json)

    print(f"encrypted {len(pages)} page(s), {pt_size} bytes plaintext -> baby.html")
    for p in pages:
        print(f"  {p['id']:<20} {p['title']}")

    if args.verify:
        out = decrypt_roundtrip(password, blob)
        assert out["pages"] == pages, "roundtrip mismatch"
        print("verify: ok")


if __name__ == "__main__":
    main()
