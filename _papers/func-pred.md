---

layout: page
title: Structure-based function prediction using graph convolution networks

---

### Structure-based function prediction using graph convolution networks

[paper](https://www.nature.com/articles/s41467-021-23303-9?sap-outbound-id=1737F1826ED10868191D41AF22CE6ACD9A144D59)
<button onClick="Copy('func-pred')">[copy link]</button>

* Very simple idea thoroughly examined.
* Protein structures often offer richer information than protein sequences, however the former are much harder to obtain and thus less available.
* Language models have been shown to yield rich embeddings of protein residues within their local context (model trained to predict residue given its neighboring residues).
* When a structure is known, sequence embeddings trained on a large corpus are used as node features and a graph convolution network yields an encoding of the contact map.
* Model is trained to predict Gene Ontology classification for proteins and shows state of the art performance.
* [Class Activation Maps](https://medium.com/@GaganaB/class-activation-maps-551477720679) are applied to trace back the importance of protein regions for the prediction.
