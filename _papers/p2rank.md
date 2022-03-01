---

layout: page
title: P2Rank, Machine Learning Based Tool for Rapid and Accurate Prediction of Ligand Binding Sites from Protein Structure
topic: Bioinformatics

---

Authors: Krivak et al.

Year: 2018

[paper](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-018-0285-8)

Given a 3D protein structure, the task is to return a list of sub-structures that are likely to accomodate a ligand (small molecule).
These sites are also known as 'pockets' or cavities.
Most popular exisitng tools include:

* Fpocket: geometric tool which filters spheres placed around the protein
* MetaPocket: Aggregates results obtained from different published algorithms
* DeepSite: deep learning model for pocket prediction. CNN Trained on structures from sc-PDB.
* SiteHound: energy-based method, probes regions on the surface for interaction strength with a force field.

Template-based methods rely on the assumption that similar protein structures will bind similar ligands.
These are most widely used methods since they will generaly give informative results that improve as more pockts are crystallized.
Template based methods face two challenges: speed and the upper bound in prediction diversity coming from the fixed library of homologous proteins to draw from.
Machine learning methods promise to resolve the dilemma between template-based and template-free methods.

Another family of approaches tries to predit binding sites at the residue level.
Each residue on the protein is treated as a binary classification task (binding/non-binding).
These are evaluated in terms of standard binary classification metrics.

There are some tradeoffs between the pocket-based and residue-based views of the task.
First, the definition of a pocket is arbitrary and residue-based methods might lead to predicting single larger pockets than many smaller ones scattered throughout the protein.

Dataset construction is also a challenge for binding site prediction.
Assuming that binding events observed in PDB represent all possible positive binding examples and the rest are negatives is highly unlikely.
This is because not seeing a protein bind a certain ligand (or observing a pocket without a ligand) could very likely be due to the fact that the protein was never exposed to the appropriate ligand.
The authors identify the CHEN11 dataset which tries to get around this problem.
CHEN11 adds positive binding sites to a given protein by mapping the structure to all homologous structures.
In other words, any protein that is found to share structural homology injects its binding sites to the current protein.
This is thought to reduce the number of false negatives.

P2Rank trains a random forest regressor on CHEN11 and other datasets by computing a vector of chemical features for points sampled around the protein and outputting a 'ligandability' score.

Performance is evaluated using the DCC score (distance between predicted pocket and nearest ligand)

Data splitting is done using SCOP such that at most 1 member per family is included in the training set. Several of the other datasets (CHEN11, JOINED, COACH420, HOLO4K) have their own splitting rules.
Others use sequence homology thresholds for splitting.


