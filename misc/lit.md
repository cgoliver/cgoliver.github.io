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
navigator.clipboard.writeText("https://carlosoliver.co/misc/quotes.html#" + id);
console.log("https://carlosoliver.co/misc/quotes.html#" + id);
}

</script>


This is a live page with my latest reading notes for various scientific topics.

---

## Bioinformatics

<div id='foldseek'>
</div>

## Foldseek: fast and accurate protein structure search

> Authors: van Kempen et al.

> Date: 2022

[paper](https://www.biorxiv.org/content/biorxiv/early/2022/02/09/2022.02.07.479398.full.pdf)
<button onclick="Copy('foldseek')">[copy link]</button>


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

