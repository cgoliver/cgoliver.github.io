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

