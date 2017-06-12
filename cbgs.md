---

layout: page
title: "CBGS"
permalink: /cbgs

---

This is the site for the **McGill Computational Biology Graduate Seminars (CBGS)**. 

We host bi-weekly talks given by graduate students about any topic related to computation and the biological sciences. Talks can be about the student's research or an interesting paper, technique or theory they would like to share with their peers. 

If you are interested in giving a talk please send me an email (carlos [dot] gonzalez [dot] oliver [at] gmail [dot] com) with you title and abstract!


<h1 class="page-heading"> Upcoming Talk </h1>

#### Faizy Ahsan

#### Title: Prediction of TF-DNA binding based on convolutional neural network architectures.

An automated tool for predicting TF-DNA binding is required
to replace time consuming and expensive lab experiments, will be relevant 
in understanding gene-regulatory networks and will be useful in tackling
TF-related diseases. Classical way to build a TF-DNA predictive model is
based on motif-finding approaches in form of consensus or PWMs. The inherent 
weakness of these models are the underlying assumption of independent nucleotide interactions in the TF-DNA binding.

Traditional machine learning TF-DNA predictive approaches outperformed classical methods by representing more generalized and flexible motifs as
k-mers and paved way for developing deep learning based methods. The state-of-the-art TF-DNA predictive methods are based on convolutionary neural networks
that use image-like patterns in sequences as motifs. However, the design of cnn architecture is challenging and is difficult to lay out the rules that are used for predictions.

In this talk, we will go through the findings of a recently published article 
'convolutional neural network achitectures for predicting DNA-protein binding [Zeng et. al, 2016]' that highlights the possibly best cnn architecture for TF-DNA 
predictive model.

**When:** Wednesday June 14th 12-1pm

**Where:** Trottier Building, Room 3120

**Food:** PIZZA!

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
