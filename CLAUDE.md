# babypedia editorial conventions

When writing or editing a `_baby_src/*.md` page, always include:

## 1. Tags

Add `tags: [...]` to the front matter using the existing taxonomy where it fits, extending only when nothing matches:

- **Stage:** `pre-birth`, `birth`, `newborn`, `first-6-months`, `6-months-plus`
- **Topic:** `sleep`, `feeding`, `diapering`, `potty`, `nutrition`, `health`, `safety`, `vaccines`, `sustainability`, `newborn-care`
- **Kind:** `principles`, `decisions`

Tags drive the click-to-filter sidebar — they're the primary cross-cutting navigation across pages.

## 2. Cross-links to other pages

Use markdown links to relevant existing pages: `[link text](#page-id)`. The page IDs are set in front matter (`id:` field). Examples:

- Always link `[manifesto](#manifesto)` when invoking the four principles.
- If you mention bathing, link `[Before Birth](#before-birth)` (which has the bath section).
- If you mention cord care, link `[Delayed Cord Clamping](#delayed-cord-clamping)`.
- If you mention vaccines, link `[Vaccines](#vaccines)`.
- Etc.

Don't force it — but if a reader on this page would benefit from another page, link it.

## 3. Images where useful

Add images from Wikimedia Commons (the only stable hotlink-friendly source) when a visual genuinely helps comprehension. Skip them for pure text/decision pages where they'd be filler.

- **Verify the URL works first** with `curl -I -A "Mozilla/5.0" <url>` — Wikimedia's thumbnailer only serves specific cached sizes (commonly 250px, 500px). 600px and odd sizes often return 400.
- Format: `![alt text](https://upload.wikimedia.org/...)`
- Add an italic caption on the line below: `*caption text*`
- Don't use brand-site or random-blog images — they break, get hotlink-blocked, or change.

## When Carlos asks a baby-related question

Default to **wiki-first**, not chat-first. The chat answer is the byproduct; the durable artifact is the wiki page.

1. **First, try to add the answer to an existing article** where it fits naturally (e.g., a sleep sack question goes into a sleep-related section, a nail scratching question into a newborn-care or first-12-weeks section). Pick the existing article whose territory most closely covers the topic and extend it there.
2. **If nothing fits, create a new article** with proper front matter (title, order, category, id, tags) following the rules above.
3. **Then summarize the answer in chat** with a one-line note about which page got the addition (or which page was created).

Trivial yes/no questions or chat-only clarifications don't need to round-trip through the wiki — use judgment. But the default is: substantive baby answer → wiki addition → chat summary, in that order.

## Workflow

Source markdown lives in `_baby_src/` (gitignored). After edits: `BABY_PASSWORD=$(cat baby.txt) python3 encrypt_baby.py` then commit `baby.html`. The full workflow detail is in the auto-memory.
