---

layout: page

---

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
 Transformer model attends to all pairs of hydrogen bonds, probably could take advantage of some sparsity there.
