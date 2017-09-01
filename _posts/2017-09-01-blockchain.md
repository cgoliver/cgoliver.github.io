---

layout: post
title: "NP-complete solving proof-of-work algorithm and blockchain"
date: 2017-09-01
comments: true

---


On the subject of using blockchain to solve scientifically interesting problems, I'd like to briefly present a [short article](https://arxiv.org/abs/1708.09419) we submitted to the arXiv recently.

In the article we outline a novel proof of work algorithm that rewards miners for solving computationally difficult puzzles while mining. 

Imagine a very simple setting where the blockchain is trying to solve some problem $P$. In this case, the problem can be stated as: Does there exist a solution $S$ to $P$ with some `score(S)` > $\gamma$?. That is, according to some agreed upon scoring scheme, can the network find a solution whose score is lower than some current best $\gamma$? Obviously for many problems, the only way to find out is by discovering such a solution. The good news is that once $S$ is identified, a key property of NP-Complete problems is that checking the score is very fast. Clearly there is a parallel between this kind of problem and [Bitcoin proof-of-work (PoW)](https://en.bitcoin.it/wiki/Proof_of_work).

We exploit this similarity by incorporating the puzzle solving into the Bitcoin PoW. Bitcoin PoW adjust mining difficulty every 2016 blocks such that on average it will always take 2 weeks to mine those 2016 blocks. Such adjustments are necessary because the mining power of the network does not remain constant and generally increases. The new puzzle-solving PoW instead allows miners to submit solutions $S$ to $P$ along with their blocks. If they submit a valid solution, their block is accepted at a lower difficulty cutoff as a reward. However, in order to maintain constant block times we enforce some constant ratio between the reduced difficulty and the Bitcoin difficulty and derive update rules accordingly. The complete details to how these rules are derived can be found in the manuscript.

The advantage of this new algorithm is that a portion of the computation power expended in blockchain mining can be redirected to interesting computations. Most importantly, we overcome the unpredictability of NP-Complete problem difficulty by approximating the difficulty with a moving empirical average. We hope that an implementation of this blockchain will lead to the maintaining and incentivization of data that is of interest to the scientific community. Any kind of NP-Complete puzzle can be used such as multiple sequence alignment, graph coloring, traveling salesman; and although not strictly an NP-complete problem, we can see applications to incentivizing the training of machine learning models.


This work was a collaboration with Alessandro Ricottone and Pericles Philippopoulos. I will be posting updates here on the development of the project.
