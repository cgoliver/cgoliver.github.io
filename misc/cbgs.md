---

layout: page

---

This is the site for the **McGill Computational Biology Graduate Seminars (CBGS)**. 

We host bi-weekly talks given by graduate students about any topic related to computation and the biological sciences. Talks can be about the student's research or an interesting paper, technique or theory they would like to share with their peers. 

If you are interested in giving a talk please send me an email (carlos [dot] gonzalez [dot] oliver [at] gmail [dot] com) with you title and abstract!


<h1 class="page-heading"> Upcoming Talk </h1>

TBA

<h1 class="page-heading">Past Talks </h1>

<ul>
  {% for post in site.talks reversed %}
  <li>
    <a href="{{ post.url }}" title="{{ post.title }}">
      <span class="date">
        <span class="day">{{ post.date | date: '%d' }}</span>
        <span class="month"><abbr>{{ post.date | date: '%b' }}</abbr></span>
        <span class="year">{{ post.date | date: '%Y' }}</span>
      </span>
      <span class="title">{{ post.title }}</span>
    </a>
  </li>
  {% endfor %}
</ul>
