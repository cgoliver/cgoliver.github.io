---

layout: page
title: REAFUM, Representative Approximate Frequent Subgraph Mining
topic: Data Mining

---

Authors: Li et al.
Year: 2015

[paper](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974010.85)


The goal is to identify subgraphs patterns with any kind of noise (not just labels or single edge deletions).
Most similar previous works are [RAM](https://link.springer.com/chapter/10.1007/978-3-540-69497-7_14) and [APGM](https://dl.acm.org/doi/pdf/10.1145/2487575.2487602) which allow for fixed number of edge removals and node label changes respectively.
In a nutshell, the algorithm selects 'representative' graphs in the dataset which are maximally distinct and then identifies subgraphs in the data that match one of the representatives.
Using GED, the authors propose a definition of the *approximate frequent subgraph mining problem*.
Given a dataset of graphs, $D$, we want to find all subgraphs in $D$ whose support is at least $\sigma$ where support is:

$$sup_{g_i} = \frac{\lvert g \in D \vert g_i \subseteq_\beta g \rvert}{\lvert D \rvert}$$

which counts the number of subgraphs in D that are isomorphic to which $g_i$ is isomorphic within $\beta$ edit operations.
The normalization factor is over the number of graphs in the dataset which could introduce soem bias towards smaller motifs or motifs which occur multiple times within the same graph.
The algorithm proposes $m$ candidate representatives and then identifies compatible instances.
For the representative selection a greedy approach which tries to maximize the distance between representatives and minimize the distance to the rest of the graphs is used.
To do this, GED would be optimal but too expensive to comptue so graphs are decomposed into bags of 'star' subgraphs (i.e node-anchored subgraphs) and matched to each other.
Evaluation is done by injecting motifs into synthetic graphs and computing retrieval accuracy on various settings of $\beta$


