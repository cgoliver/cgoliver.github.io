<div id='foldseek'>
</div>

### Foldseek: fast and accurate protein structure search 


<button onclick="Copy('foldseek')">[copy link]<button>

> Authors: van Kempen et al.

> Date: 2022

[paper](https://www.biorxiv.org/content/biorxiv/early/2022/02/09/2022.02.07.479398.full.pdf)


* Given a query protein 3D structure and a protein database, return the most similar structures to the query in the database.
* Established tools for this task are: DALI, and TMAlign
* Both perform a kind of matching between structures. Dali works on matching contact maps, and TMAlign directly on structures. The resulting matchings tend to favor global compatibility and have the disadvantage of being computationally expensive.
* Foldseek tries to propose a search system that can scale to databases of millions of protein structures.
* The idea is to flatten a 3D structure into a sequence (similar to 3DBLAST) since searching over sequences is fast.
* Unlike the 3DBLAST method which encodes backbone conformations into the sequence, Foldseek includes contact information (i.e. the conformation of the contact between the residue being encoded and its nearest neighbor in 3D space)
* The types of conformations are binned into 20 categories to give rise to a 'conformation alphabet'
* This results in a mapping from 3D structures to sequences with an augmented alphabet.
* Given a query, a BLAST filtering narrows down promising candidates, and the hits are refined using Smith-Waterman sequence alignment.
* SCOP is used to evaluate the retrieval accuracy of the tool.
* Manual inspection suggests that Foldseek is able to recover locally matching structures.

