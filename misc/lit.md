---

layout: page

---

*This is a live page with my latest reading notes for various scientific topics.*

---


{% assign items_grouped = site.papers | group_by: 'topic' %}
{% for group in items_grouped %}
## {{group.name}}
{% for item in group.items %}
* [{{item.title}}]({{ item.url }})
{% endfor %}
{% endfor %}
