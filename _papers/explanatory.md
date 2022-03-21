---

layout: page
title: Explanatory Learning, Beyond Empricism in Neural Networks 
topic: Machine Learning 

---

Authors: Mariani et al.

Date: 2022 

[paper](https://arxiv.org/pdf/2201.10222.pdf)


A universe $U$ is a subset of phenomena $P_1, P_2, P_3, ..$, the universe has no particular structure other than it is a set of possible observations $U = \{x_1, .., x_z\}$. A **language** is a set of strings $\Sigma_L$ over an alphabet $|A|$ paired with a binary function $\mathcal{I}_L$ which assigns a binary value to any string-observation pair in the universe and language. The binary function is called an **interpreter**. A phenomenon $P_i$ is **explainable** in a language L if there exists a string $e \in \Sigma_L$ such that for any observation $x \in U$, the iterpreter function evaluated at $x$ and $e$ is True whenever $x$ belongs to phenomenon $P_i$: $\mathcal{I}_L(x, e) = 1_{P_i(x)}$. In other words, an explanation is able to identify observations that are part of a given phenomenon.

