---

layout: page
title Representation Learning for Frequent Subgraph Mining
topic: Data Mining

---

Authors: Rex Ying et al.
Date: 2021


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

