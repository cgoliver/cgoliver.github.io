---

layout: page
title: Populations of genetic circuits are unable to find the fittest solution in a multilevel genotype-phenotype map
topic: Theoretical Biology

---

Authors: Catalan et al.

Year: 2020

[paper](https://auditore.cab.inta-csic.es/manrubia/files/2020/09/JRSI17-20190843.pdf)

This paper proposes a toy model of Gene Regulatory Networks (GRNs) with the aim of understanding the genotype-phenotype map at the level of network topology.
The toy model consists of two genes, A and B and is described by whether each gene is expressed or not, and the effect that one expressed protein has on the other (activation/inhibition).
As an additional layer of complexity, the model includes a 'one dimensional tissue' consisting of a row of cells.
Each cell expresses the genes, and protein A is allowed to diffuse to neighboring cells. 
When the dynamics are simulated over time and space, we can observe the expression pattern of genes A and B.
The authors use this pattern as a 'phenotype' and the expression/interaction specification of the GRN ad a genotype.
To define a fitness, we choose a specific expression pattern (e.g. protien A is always expressed in all cells) and define a distance function between any two patterns.
Genotypes that lead to patterns similar to the 'target' pattern are given a higher fitness and with this an evolutionary algorithm is possible.

Unfolding the evolutionary algorithm on a specific pattern shows that the abundance of a given genotype dominates the degree to which it fixes in the population.
That is, despite some genotypes leading to higher fitness, these are often not found.
Additionally, different genotypes with the same fitness are not equally fixed in the population, again due to the abundance of the genotype in the space.
This is likely shaped by the complexity of the pattern and its connectivity to other genotypes.

