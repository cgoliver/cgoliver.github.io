---

layout: page
title: Assessment of ligand binding site predictions in CASP10
topic: Bioinformatics

---

Authors: Gallo Cassarino et al.

Year: 2013

[paper](https://onlinelibrary.wiley.com/doi/10.1002/prot.24495)

An additional challenge was proposed for CASP20.
In addition to predicting the 3D structure blindly for a protein sequence, contestants were also asked to predict the residues which would bind a small molecule ligand.
Interestingly, the authors note that the crystallization process sheds low-moderate binding affinities and thus when we see a ligand binding event it is likely to have a strong affinity to the pocket.

A binding site is defined as the set of residues having at least one non-hydrogen atom within a certain distance to biologically relvant ligand atoms.

*Evaluation of binding site prediction.* Contestants were asked to classify each residue of the protein as binding or non-binding. 
These predictions are compared with the binding site obtained according to the above definition.
With this, the Matthews Correlation Coefficient is obtained:

$$ MCC = \frac{TP \timesTN - FP \times FN}{\sqrt{(TP + FP) \times (TP + FN) + (TN + FP) \times (TN + FN)}} $$

Since there were several targets in the prediction, multiple MCCs are combined using a Z-score with respect to the average MCC and the standard deviation of MCCs.
Using this combined statistic, a final performance score is obtained.

This challenge was being maintained as part of [CAMEO](https://www.cameo3d.org/ligand-binding/) but was discontinued in 2016.
