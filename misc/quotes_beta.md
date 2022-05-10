---

layout: page

---

*This is a live page with collected quotes

---


{% for author in site.quotes %}
* {{author.name }}
{% endfor %}
