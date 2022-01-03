---

layout: page

---

This is a live page with my latest reading notes for various scientific topics.

## Bioinformatics

### Protein Structure Comparison by Alignment of Distance Matrices 

> Authors: Liisa Holm and Chris Sander 
> Date: 1993 

[paper](http://www.marcottelab.org/users/CH391L/Handouts/dali.pdf)

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

### Hydrogen bonds meet self-attention: all you need for general-purpose protein structure embedding.

[paper](https://www.biorxiv.org/content/10.1101/2021.01.31.428935v2.full.pdf)

*Methods*

* Neural network architectureis proposed to encode protein 3D structures based on local and global information.
* First, all pairs of residues connected by hydrogen bonds are extracted. A $k$ residue window along the backbone of each residue is added for contact. An MLP is then used to encode the corresponding carbon-alpha distance matrix into a fixed-size embedding.
* Once an embedding for each bond is computed, a transformer with all-to-all attention is used to pool the embeddings into a single global embedding.
* The model is trained end-to-end on the [SCOP](https://scop.berkeley.edu/) protein classification. That is, embeddings are trained to be able to predict the structural family of a given protein.
* Authors show that state of the art performance on SCOP classification is achieved, and that a good correlation with TM-score when using embeddings to retrieve structurally similar proteins is also achieved.

*Comments*

* The model still requires external supervision to work, so the claim that this is a 'general purpose' embedding is somewhat misleading.
* Transformer model attends to all pairs of hydrogen bonds, probably could take advantage of some sparsity there.

### Structure-based function prediction using graph convolution networks

[paper](https://www.nature.com/articles/s41467-021-23303-9?sap-outbound-id=1737F1826ED10868191D41AF22CE6ACD9A144D59)

* Very simple idea thoroughly examined.
* Protein structures often offer richer information than protein sequences, however the former are much harder to obtain and thus less available.
* Language models have been shown to yield rich embeddings of protein residues within their local context (model trained to predict residue given its neighboring residues).
* When a structure is known, sequence embeddings trained on a large corpus are used as node features and a graph convolution network yields an encoding of the contact map.
* Model is trained to predict Gene Ontology classification for proteins and shows state of the art performance.
* [Class Activation Maps](https://medium.com/@GaganaB/class-activation-maps-551477720679) are applied to trace back the importance of protein regions for the prediction.

## Biology

## General Machine Learning

## Graph Machine Learning

### Representation Learning for Frequent Subgraph Mining

> Authors: Rex Ying et al.
>> Date: 2021

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


## Graph Theory

## Reinforcement Learning

