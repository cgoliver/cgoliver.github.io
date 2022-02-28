---

layout: page
title: Protein Structure Comparison by Alignment of Distance Matrices

---

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

