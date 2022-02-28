---

layout: page

---

*This is a live page with my latest reading notes for various scientific topics.*

---

## Bioinformatics


[Protein Structure Comparison by Alignment of Distance Matrices]({{ site.url  }}/misc/papers/dali.md) 

{% include_relative papers/foldseek.md %}

{% include_relative papers/scones.md %}

{% include_relative papers/hydrogen.md %}

{% include_relative papers/dali.md %}


### Towards Effective and Generalizable Fine-Tuning for Pre-trained Molecular Graph Models

[paper](https://www.biorxiv.org/content/biorxiv/early/2022/02/06/2022.02.03.479055.full.pdf)


### Subgraph Augmentation with Application to Graph Mining

[paper](https://link.springer.com/chapter/10.1007/978-981-16-2609-8_4)

### Sampling Subgraph Network With Application to Graph Classification


[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9547804)

<div id='sp-miner'></div>
### Representation Learning for Frequent Subgraph Mining

> Authors: Rex Ying et al.

> Date: 2021

<button onClick="Copy('sp-miner')">[copy link]</button>

*Background:* The goal here is to identify subgraphs that have some minimum number of occurrences in a set of graphs.
Hence, a motif in this context is a specific subgraph with a certain number of occurrences.
Counting subgraph instances is NP-Hard so methods for doing this use approximations.
The authors propose a method of doing this efficiently with the use of representation learning. 

*Results:* The key trick here is to train a model to generate an *ordered embedding space*. 
In this case, ordering in the embedding space encodes subgraph/supergraph relations. 
Hence, if an embedding of a given subgraph is `smaller' than an oter this means that it is a subgraph of the larger embedding.
Once a dataset is embedded in such a manner, we can very efficiently know how many graphs have a certain graph as a subgraph, and hence an approximate number of occurrences.
An iterative method for obtaining motifs is then proposed which moves through the embedding space, collecting subgraphs with sufficient occurrences.

The main limitations are that there is no statistical notion of sufficient representation, and the notion of structural similarity between motifs is not dealt with.
Additionally, the use of GCNs as the representation function and training method make it such that the type of motif recoverable is of a certain structure, namely a `node-anchored subgraph'. 

<div id='gromov'></div>
### Scalable Gromov-Wasserstein Learning for Graph Partitioning and Matching

> Authors: Xu et al.

> Date: 2019 

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

### Motif-Aware Adversarial Graph Representation Learning

> Authors: Zhao et al.

> Year: 2022

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9684408)


### Self-Supervised Graph Transformer on Large-Scale Molecular Data

[paper](https://arxiv.org/pdf/2007.02835.pdf)

## Graph Theory

<div id="wass"></div>
### Approximate Graph Mining with Label Costs

> Authors: Anchuri et al.

> Year: 2013

[paper](https://dl.acm.org/doi/pdf/10.1145/2487575.2487602)

<button onClick="Copy('wass')">[copy link]</button>

Most motif mining papers try to find patterns (motifs) that are isomorphic to a large number of subgraphs in a dataset of graphs.
Here, the authors ateempt to relax the constraint in the setting where nodes have a 'label' and allow motifs to match subgraphs with some discrepancy in the node labels. 

Graphs are associated with a cost matrix $C[l_i][l_j]$ gives the cost of matching node label $l_i$ to $l_j$ where each graph has a vector of node labels $L$.
A motif is represented as a 'pattern graph' which is isomorphic to some subgraphs of the whole dataset such that some function $\phi$ is an injective mapping from the pattern graph nodes $G_P$ to some subgraph of the data $V_S$.
This means that instances of $G_P$ will be isomorphic to it, but to allow for some flexibility, an isomorpic mapping can have some cost $C(\phi) = \sum_{u \in V_P} C[L(u)][L(\phi(u))]$, or the sum of label substitution costs.
The *support* of a pattern is a function of the number of occurrences of the pattern in the data which can be defined in different ways.
The *representative set* of a node is the set of nodes that map to it.
The overall approach is then to generate possible pattern graphs and compute its support, and yield the representative set of all the patterns with large support.
Of course enumerating all possible patterns grows exponentially with the size of the pattern.
Intead, patterns are generated by randomly adding edges to an initial seed node in a depth-first manner.
The edges are extended as long as the pattern has sufficient support and abandoned otherwise.
Evaluation consists mostly of showing that the algorithm is able to return patterns with a given support level within some time limit.
Pattern size appears to be sufficiently large.



### ASAP: Fast, Approximate Graph Pattern Mining at Scale


> Authors: Iyer et al.

> Year: 2018


[paper](https://www.usenix.org/system/files/osdi18-iyer.pdf)


<div id='reafum'></div>
### REAFUM: Representative Approximate Frequent Subgraph Mining

> Authors: Li et al.

> Year: 2015

[paper](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974010.85)

<button onclick="Copy('reafum')">[copy link]</button>

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


### Ap-FSM: A parallel algorithm for approximate frequent subgraph mining using Pregel

[paper](https://www.sciencedirect.com/science/article/pii/S0957417418302409?casa_token=nOi8L-oTtdAAAAAA:jZiYPorKCqA-vD-S4vRk_NC6EdRrrJWwQ8X8B9Rl_3IsVKOpbPbH1SGvObNr2BP5gsvKhijrPqY)


### A survery of frequent subgraph mining algorithms

[paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A58904230A6680001F17FCE91CB8C65F/S0269888912000331a.pdf/survey_of_frequent_subgraph_mining_algorithms.pdf)


<div id="maniacs"></div>
### ManIACS: Approximate Mining of Frequent Subgraph Patterns through Sampling

> Authors: Preti et al.

> Year: 2021

[paper](https://dl.acm.org/doi/pdf/10.1145/3447548.3467344)

<button onclick="Copy('maniacs')">[copy link]</button>

The problem is called 'Frequent Subgraph Pattern Mining' (FSPM) in which a single graph is mined for the most frequent small graph patterns. 
A *pattern set* for a fixed size $k$ is the set of all possible *connected* graphs with up to $k$ vertices.
Using a specific frequency definition, the tool is able to prune *pattern space* to compute exact patterns with a large frequency.
The algorithm is limited to working on a single graph.



### TKG: Efficient Mining of Top-K Frequent Subgraphs

[paper](http://www.philippe-fournier-viger.com/2019_BDA_TKG_Top-k-subgraphs.pdf)


### MARGIN: Maximal Frequent Subgraph Mining

[paper](https://dl.acm.org/doi/pdf/10.1145/1839490.1839491)


### Frequent subgraph mining for biologically meaningful structural motifs

> Authors: Keller et al.

> Year: 2020

[paper](https://www.biorxiv.org/content/10.1101/2020.05.14.095695v1.full.pdf)



### Large graph sampling algorithm for frequent subgraph mining

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9456952)

### Pangolin: An efficient and flexible graph mining system on CPU and GPU

[paper](https://dl.acm.org/doi/pdf/10.14778/3389133.3389137)


### G-Finder: Approximate Attributed Subgraph matching

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9006525&casa_token=YCeHeY_6yVMAAAAA:wimWLdTB2NrnGo4MX20on-29kDLzIiuwWoHF5uZN8UFsg89MzMB_x6y_xSYGxfS7QKRNM8cFrA&tag=1)

> Authors: Liu et al.

> Year: 2019

Proposes data structures and search algorithms for retrieving the top $k$ most similar subgraphs given a query graph.
The algorithm allowes for some inexact matching such as missing nodes or edges.

### Extension of Canonical Adjacency Matrices for Frequent Approximate Subgraph Mining on Multi-Graph Collections

[paper](https://www.worldscientific.com/doi/pdf/10.1142/S0218001417500252?casa_token=7ivI3tIMuroAAAAA:UJYDJK7x9fZsbvUf1yUw66uJtFL-PZLqgP5Q3ZA57Kcu0seTUHe63GHlEf813K24XoVPqlcBqMNJ)

### An Efficient System for Subgraph Discovery

[paper](https://ieeexplore.ieee.org/abstract/document/8622126?casa_token=-ggWYIFBr5UAAAAA:oBHVjU2431vhZ9NcxwNhEi61vJ-Y41IBidKlJMcPC-2yyk_tPDt8MV-Q8512QSIZZKIEogcT-g)

### Efficiently mining recurrent substructures from protein three-dimensional structure graphs

[paper](https://www.liebertpub.com/doi/full/10.1089/cmb.2018.0171)


### Frequent pattern mining in big social graphs

[paper](https://ieeexplore.ieee.org/abstract/document/9395505?casa_token=pflfaIYzMw8AAAAA:kaj7b1HSztGLjlTbJ5SQNeYbn6oV-eoF80kURwUvQpwJ0xZSGnofgdSny6D7kU3E73yO6lZkMg)

### Motifs in temporal networks

[paper](https://dl.acm.org/doi/abs/10.1145/3018661.3018731)


### Efficient sampling algorithm for estimating subgraph concentrations and detecting network motifs

[paper](https://academic.oup.com/bioinformatics/article/20/11/1746/300212?login=true)


## Cheminformatics

