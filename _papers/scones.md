---

layout: page
title: Efficient network-guided multi-locus association mapping with graph cuts
topic: Bioinformatics

---

Authors: Azencott et al.
Date: 2013

[paper](https://academic.oup.com/bioinformatics/article/29/13/i171/198210)

* Genome-wide association studies use genomic sequences from multiple individuals for which a given phenotype is known to compute the degree to which a given single-nucleotide polymorphism is associated to the phenotype.
* Usually, the association is expressed as a p-value.
* Typically, combinations of SNPs are involved in the phenotype, however p-values are known only for individual SNPs.
* Testing all possible combinations of SNPs is computationally prohibitive, so we need some priors to limit the search space.
* In this work, network-based priors are explored.
* A network-based prior only considers combinations of SNPs according to some underlying interaction criterion (e.g. only consider SNPs that correspond to genes known to share a physical interaction)
* We can think of this process as taking a biological network (Gene-gene interaction network) and introducing the p-value as a feature in each node.
* The task is then to find a connected subgraph such that the sum of p-valued (additive assumption) is maximal.
* Here, the p-value of a node is denoted as $c_i$
* From these criteria we get the following optimization problem for a network of $n$ SNPs

$$ argmax_{f \in \{0, 1\}^n} c^Tf - \lambda f^TLf - \eta || f ||_0$$ 

where $f_i$ is 1 if node $i$ is selected and 0 otherwise. The first term controls the additive significance of the seleted nodes, the second term penalizes disconnected subgraphs since it depends on the graph Laplacian $L$, and the final term is a sparsity constraint since the additive term will encourage selecting all nodes.
* By rewriting some terms, the optimization is expressed as a min-cut problem over the same graph with two auxilliary nodes inserted $s, t$.
* $s$ is connected to all nodes with a p-value above a threshold $\eta$ and $t$ to all nodes below the threshold.
* Min-cut max flow solvers can then be used and the resulting $f$ tells us which nodes were selected.
