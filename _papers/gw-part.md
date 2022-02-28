---

layout: page
title: Scalable Gromov-Wasserstein Learning for Graph Partitioning and Matching
topic: Graph Machine Learning

---

Authors: Xu et al.
Date: 2019 

[paper](https://proceedings.neurips.cc/paper/2019/file/6e62a992c676f611616097dbea8ea030-Paper.pdf)
<button onClick="Copy('gromov')">[copy link]</button>

* Gromov-Wasserstein discrepancy between graphs is a soft mapping from nodes in $G_s$ to $G_t$ which minimizes a cost on pairs of nodes mapped to each other which can be iteratively minimized.
* The mapping is done in order to minimize the optimal transport between two node 'distributions' which typically reflect the degree distribution of the nodes in two graphs.
* Using this distance, two other concepts are introduced: graph partitioining, and barycenter computation.

$$ d_{gw}(G_s, G_t) = \min_{\bf T \in \Pi(\bf \mu_s, \bf \mu_t)} \bigg( \sum_{i, j \in \mathcal{V}_s} \sum_{i', j' \in \mathcal{V}_t} \lvert c_{ij}^s - c_{i' j'}^t \rvert^{p} \bf T_{ii'} \bf T_{jj'} \bigg) $$

where $$\Pi(\bf \mu_s, \bf \mu_t) = \{ \bf T \geq \bf 0 \vert \bf T1_{\lvert \mathcal{V}_t \rvert} = \bf \mu_s,  \bf T^{T} \bf 1_{\lvert \mathcal{V}_s \rvert} = \bf \mu_t \}$$

The double summation reads as: for each pair of nodes $i, j$ in the nodes of $G_s$, look at each pair of nodes $i', j'$ in $G_t$ and compute a score. 
The first term in score is given by the difference in adjacency between $i, j$ and $i', j'$. 
So the absolute value term is zero when the pair of nodes in $G_s$ and in $G_t$ being looked at is eithr both adjacent or non-adjacent.
This adjacency term which looks at the original graphs adjacency matrices $C$, is multiplied by the mapping state of the pairs, $\bf T$.
So the term $T_{ii'}$ gives us the probability that $i \in G_s$ is assigned to $i' in G_t$.
When this probability is large for both pairs of nodes, i.e. $i, j$ both have a high probability of being mapped to some $i', j'$, we punish discrepancies in their adjacency status, as measured by $\lvert c_{ij}^s - c_{i'j'}^t \rvert$.
Of course this can be hacked by just making $\bf T \rightarrow \bf 0$ but this term is excluded in the search set $\Pi(\bf \bf \mu_s, \bf \mu_t)$ by only choosing $\bf T$ that assign probability from each node in $G_s$ to every other node in $G_t$.


* Solving this distance is non-convex and the authors use a proximal gradient method to decompose the problem into smaller convex ones. 
* Graph partitioning is traditionally done by identifying subgraphs which have high connectivity within itself and low connectivity to the rest of the graph. This is also known as 'modularity'.
* If we think of each 'module' as forming a single 'super node' then a partitioned graph corresponds to a set of disconnected 'super nodes'.
* To use GW distance for graph partitioning, one tries to identify a mapping from the given graph to a disconnected graph of $K$ nodes.
* Graph partitioning can be applied recurively. Once the nodes are partitioned, apply a matching step across nodes assigned to the same 'super node' and then partition within the 'super node'. This helps with scalability.
* Authors find a strong sensitivity to hyperparameters but promising accuracy on large graph alignment tasks. 


Relevant literature:

* [Wasserstein-based Graph Alignment](https://arxiv.org/pdf/2003.06048.pdf)
