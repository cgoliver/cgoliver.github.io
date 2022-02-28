---

layout: page

---

### Learning structural motif representations for efficient protein structure search

[paper](https://dl.acm.org/doi/pdf/10.1145/974614.974655)

<div id='deepfold'></div>

> Authors: Liu et al.

> Date: 2018

[paper](https://academic.oup.com/bioinformatics/article/34/17/i773/5093231?login=false)

We can compare protein structures in two ways: alignment-based, and alignment-free.
One of the most widely-used alignment methods is [TMalign](https://academic.oup.com/nar/article-abstract/33/7/2302/2401364), which tries to explicitly superimpose two proteins on each other while minimizing a discrepancy score.
The problem with alignment-based methods is that they often do not scale when trying to compare many structures against each other which is the setting in structure retrieval.
Alignment-free methods instead encode protein structures into a vector space where comparisons are very quick.


Related work:

* [TMalign](https://academic.oup.com/nar/article-abstract/33/7/2302/2401364)
* [FragBag](https://www.pnas.org/content/107/8/3481.short)
