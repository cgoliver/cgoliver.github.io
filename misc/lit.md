---

layout: page

---

<style>
button {
    background-color: Transparent;
    background-repeat:no-repeat;
    border: none;
    cursor:pointer;
    overflow: hidden;
    outline:none;
    color: #a00;
}
button:focus{
   color:#595959;
}
</style>

<script>
function Copy(id){
navigator.clipboard.writeText("https://carlosoliver.co/misc/lit.html#" + id);
console.log("https://carlosoliver.co/misc/quotes.html#" + id);
}

</script>


*This is a live page with my latest reading notes for various scientific topics.*

---

## Bioinformatics

### Learning structural motif representations for efficient protein structure search

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



<div id='foldseek'>
</div>

### Foldseek: fast and accurate protein structure search 


<button onclick="Copy('foldseek')">[copy link]<button>

> Authors: van Kempen et al.

> Date: 2022

[paper](https://www.biorxiv.org/content/biorxiv/early/2022/02/09/2022.02.07.479398.full.pdf)


* Given a query protein 3D structure and a protein database, return the most similar structures to the query in the database.
* Established tools for this task are: DALI, and TMAlign
* Both perform a kind of matching between structures. Dali works on matching contact maps, and TMAlign directly on structures. The resulting matchings tend to favor global compatibility and have the disadvantage of being computationally expensive.
* Foldseek tries to propose a search system that can scale to databases of millions of protein structures.
* The idea is to flatten a 3D structure into a sequence (similar to 3DBLAST) since searching over sequences is fast.
* Unlike the 3DBLAST method which encodes backbone conformations into the sequence, Foldseek includes contact information (i.e. the conformation of the contact between the residue being encoded and its nearest neighbor in 3D space)
* The types of conformations are binned into 20 categories to give rise to a 'conformation alphabet'
* This results in a mapping from 3D structures to sequences with an augmented alphabet.
* Given a query, a BLAST filtering narrows down promising candidates, and the hits are refined using Smith-Waterman sequence alignment.
* SCOP is used to evaluate the retrieval accuracy of the tool.
* Manual inspection suggests that Foldseek is able to recover locally matching structures.

<div id='scones'>
</div>
## Efficient network-guided multi-locus association mapping with graph cuts

> Authors: Azencott et al.

> Date: 2013

[paper](https://academic.oup.com/bioinformatics/article/29/13/i171/198210)
<button onclick="Copy('scones')">[copy link]</button>

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



<div id='dali'>
</div>

### Protein Structure Comparison by Alignment of Distance Matrices 

> Authors: Liisa Holm and Chris Sander 

> Date: 1993 

[paper](http://www.marcottelab.org/users/CH391L/Handouts/dali.pdf)
<button onclick="Copy('dali')">[copy link]</button>

*Background:*  Aligning 3D structures of proteins is crucial for discovering functional sub-structures, protein classification, and understanding new proteins.
At the time of writing, this paper was among the first to propose a general tool for comparing solved 3D structures of proteins.
The exact alignment problem is NP-Hard, hence the authors propose an approximate method.

*Results:* This work presents DALI, which is still a widely used protein-protein alignment tool.
The algorithm performs matching of distance matrices between two proteins.
To prune the search space, DALI extracts contiguous blocks of 6 amino acids from the distance matrices of each protein.
These blocks form the objects which are to be matched so as to minimize a penalty function applied to matched blocks $i, j$:

$$ S = \sum_{i}^{L} \sum_{j}^{L} \phi(i, j) $$

Typically, $\phi$ is a function of the intra-residue distance of the matched blocks with some normalizations.
To obtain a full alignment, a seed match is chosen and extended through a monte carlo search.
This process is of course not guaranteed to identify the global minimum, and is sensitive to starting conditions.
However, the authors repeat the process and show that the algorithm remains quite robust and finds alignments close to the global optimum.

<div id='hydrogen'></div>
### Hydrogen bonds meet self-attention: all you need for general-purpose protein structure embedding.

[paper](https://www.biorxiv.org/content/10.1101/2021.01.31.428935v2.full.pdf)
<button onclick="Copy('dali')">[copy link]</button>

*Methods*

* Neural network architectureis proposed to encode protein 3D structures based on local and global information.
* First, all pairs of residues connected by hydrogen bonds are extracted. A $k$ residue window along the backbone of each residue is added for contact. An MLP is then used to encode the corresponding carbon-alpha distance matrix into a fixed-size embedding.
* Once an embedding for each bond is computed, a transformer with all-to-all attention is used to pool the embeddings into a single global embedding.
* The model is trained end-to-end on the [SCOP](https://scop.berkeley.edu/) protein classification. That is, embeddings are trained to be able to predict the structural family of a given protein.
* Authors show that state of the art performance on SCOP classification is achieved, and that a good correlation with TM-score when using embeddings to retrieve structurally similar proteins is also achieved.

*Comments*

* The model still requires external supervision to work, so the claim that this is a 'general purpose' embedding is somewhat misleading.
* Transformer model attends to all pairs of hydrogen bonds, probably could take advantage of some sparsity there.

<div id='func-pred'></div>
### Structure-based function prediction using graph convolution networks

[paper](https://www.nature.com/articles/s41467-021-23303-9?sap-outbound-id=1737F1826ED10868191D41AF22CE6ACD9A144D59)
<button onClick="Copy('func-pred')">[copy link]</button>

* Very simple idea thoroughly examined.
* Protein structures often offer richer information than protein sequences, however the former are much harder to obtain and thus less available.
* Language models have been shown to yield rich embeddings of protein residues within their local context (model trained to predict residue given its neighboring residues).
* When a structure is known, sequence embeddings trained on a large corpus are used as node features and a graph convolution network yields an encoding of the contact map.
* Model is trained to predict Gene Ontology classification for proteins and shows state of the art performance.
* [Class Activation Maps](https://medium.com/@GaganaB/class-activation-maps-551477720679) are applied to trace back the importance of protein regions for the prediction.

## Graph Machine Learning

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

## Graph Theory

### Approximate Graph Mining with Label Costs

> Authors: Anchuri et al.

> Year: 2013

[paper](https://dl.acm.org/doi/pdf/10.1145/2487575.2487602)

Most motif mining papers try to find patterns (motifs) that are isomorphic to a large number of subgraphs in a dataset of graphs.
Here, the authors ateempt to relax the constraint in the setting where nodes have a 'label' and allow motifs to match subgraphs with some discrepancy in the node labels. 

Graphs are associated with a cost matrix $C[l_i][l_j]$ gives the cost of matching node label $l_i$ to $l_j$ where each graph has a vector of node labels $L$.
A motif is represented as a 'pattern graph' which is isomorphic to some subgraphs of the whole dataset such that some function $\phi$ is an injective mapping from the pattern graph nodes $G_P$ to some subgraph of the data $V_S$.
This means that instances of $G_P$ will be isomorphic to it, but to allow for some flexibility, an isomorpic mapping can have some cost $C(\phi) = \sum_{u \in V_P} C[L(u)][L(\phi(u))]$, or the sum of label substitution costs.
The *support* of a pattern is a function of the number of occurrences of the pattern in the data which can be defined in different ways.
The *representative set* of a node is the set of nodes that map to it.
The overall approach is then to generate possible pattern graphs and compute its support, and yield the representative set of all the patterns with large support.
Of course enumerating all possible patterns grows exponentially with the size of the pattern.



### ASAP: Fast, Approximate Graph Pattern Mining at Scale


> Authors: Iyer et al.

> Year: 2018


[paper](https://www.usenix.org/system/files/osdi18-iyer.pdf)


### REAFUM: Representative Approximate Frequent Subgraph Mining

[paper](https://epubs.siam.org/doi/pdf/10.1137/1.9781611974010.85)


### Ap-FSM: A parallel algorithm for approximate frequent subgraph mining using Pregel

[paper](https://www.sciencedirect.com/science/article/pii/S0957417418302409?casa_token=nOi8L-oTtdAAAAAA:jZiYPorKCqA-vD-S4vRk_NC6EdRrrJWwQ8X8B9Rl_3IsVKOpbPbH1SGvObNr2BP5gsvKhijrPqY)


### A survery of frequent subgraph mining algorithms

[paper](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/A58904230A6680001F17FCE91CB8C65F/S0269888912000331a.pdf/survey_of_frequent_subgraph_mining_algorithms.pdf)


### ManIACS: Approximate Mining of Frequent Subgraph Patterns through Sampling

[paper](https://dl.acm.org/doi/pdf/10.1145/3447548.3467344)


### TKG: Efficient Mining of Top-K Frequent Subgraphs

[paper](http://www.philippe-fournier-viger.com/2019_BDA_TKG_Top-k-subgraphs.pdf)


### MARGIN: Maximal Frequent Subgraph Mining

[paper](https://dl.acm.org/doi/pdf/10.1145/1839490.1839491)


### Frequent subgraph mining for biologically meaningful structural motifs


[paper](https://www.biorxiv.org/content/10.1101/2020.05.14.095695v1.full.pdf)

### Large graph sampling algorithm for frequent subgraph mining

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9456952)

### Pangolin: An efficient and flexible graph mining system on CPU and GPU

[paper](https://dl.acm.org/doi/pdf/10.14778/3389133.3389137)


### G-Finder: Approximate Attributed Subgraph matching

[paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=9006525&casa_token=YCeHeY_6yVMAAAAA:wimWLdTB2NrnGo4MX20on-29kDLzIiuwWoHF5uZN8UFsg89MzMB_x6y_xSYGxfS7QKRNM8cFrA&tag=1)

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

