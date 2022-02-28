---

layout: page
title: ProteinNet, a standardized data set for machine learning of protein structure
topic: Bioinformatics

---

Author: Mohammed AlQuraishi
Year: 2019

[paper](https://bmcbioinformatics.biomedcentral.com/track/pdf/10.1186/s12859-019-2932-0.pdf)

ProteinNet is a dataset of protein sequences for which the 3D structure is known.
The dataset is used to evaluate the performance of ML-based structure prediction methods.
Non-redundant splits in the sequence side are obtained through clustering and multiple sequence alignments.
The splits are applied to different time points in the history of CASP.
That is, the dataset is created at various time intervals which represent different 'snapsots' of the PDB.
Models that perform well on earlier snapshots would be those that can work with smaller dataset sizes.

