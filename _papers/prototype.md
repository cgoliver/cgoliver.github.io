---

layout: page
title: Prototypical Networks for Few-shot Learning
topic: Machine Learning 

---

Authors: Snell et al. 

Date: 2017 

[paper](https://proceedings.neurips.cc/paper/2017/file/cb8da6767461f2812ae4290eac7cbc42-Paper.pdf)

**Few-shot learning**: prediction setting where a classifier is asked make predictions on classes not seen or seen a few times in training. 

Related work: Matching newtorks in whcih learned embeddings are matched using attention between labeled and unlabeled points. [paper](https://proceedings.neurips.cc/paper/2016/file/90e1357833654983612fb05e3ec9148c-Paper.pdf) 

This work proposes the inductive bias that there exists a single representation (prototype) for all the points of a given class, and that a new point can be classified by matching a new point to the closest prototype.
In the few-shot setting, several points (support set) of a given class are known, and in a zero-shot no examples are known, but some 'meta data' about the class is used instead.

![]({{site.url}}/assets/prototype.png)

Embeddings are optimized to maximize the probability of the true class given the embeddings. 
This probability is computed as a softmax over the distances from a given point $x$ and the prototype vectors of each class.
In turn, the prototype vectors are a simple aggregation of all the points of the same class.
