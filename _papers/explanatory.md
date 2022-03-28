---

layout: page
title: Explanatory Learning, Beyond Empricism in Neural Networks 
topic: Machine Learning 

---

Authors: Mariani et al.

Date: 2022 

[paper](https://arxiv.org/pdf/2201.10222.pdf)


A universe $U$ is a subset of phenomena $P_1, P_2, P_3, ..$, the universe has no particular structure other than it is a set of possible observations $U = \{x_1, .., x_z\}$. A **language** is a set of strings $\Sigma_L$ over an alphabet $|A|$ paired with a binary function $\mathcal{I}_L$ which assigns a binary value to any string-observation pair in the universe and language. The binary function is called an **interpreter**. A phenomenon $P_i$ is **explainable** in a language L if there exists a string $e \in \Sigma_L$ such that for any observation $x \in U$, the iterpreter function evaluated at $x$ and $e$ is True whenever $x$ belongs to phenomenon $P_i$: $\mathcal{I}_L(x, e) = 1_{P_i(x)}$. In other words, an explanation is able to identify observations that are part of a given phenomenon. 

The authors develop a playground for this concept using simple geometric shapes on a fixed-size array. We can observe instances of a phenomenon as arrangements of shapes on the array. 

![]({{site.url}}/assets/el.png)

Arrangements that follow a common 'rule' are said to belong to the same phenomenon. In the example below, the rule/explanation is 'at least one square at the right of a red pyramid'. Here, the phenomeon is the set of all arrangements following this rule. An interpreter is a function that takes an explanation and an arrangement and decides whether or not it belongs to the phenomenon. Since this phenomeon is explainable (we just gave its explanation) we know that evaluating the interpreter on the all possible arrangements will give us the whole set of occurrences of this phenomenon.

The authors define several problems using this framework where we can be given multiple phenomena, explanations to some phenomena and not others, and partial sets of observations for said phenomena. The goal is usually to train a model that can accept an obeservation and determine whether it belongs to a given phenomenon, and going futher be able to generate explanations that satisfy an interpreter. 

Different approaches to this problem hint at debates in epistemology. For example, an approach that only works with occurrences and directly tries to map them to a correct interpretation would be called fully empirical since it assumes that all necessary knowledge can be derived from observations (i.e. data). Whereas a 'rationalist' approach tries to generate explanations before seeing the observations, and these observations are tested on data and updated. The authors formaize the rationalist approach in terms of deep learning architectures as 'Critical Rationalist Networks'. These models are built on language transformer models which generate English sentences as possible explanations which are fed to a decoder that determines whether the explanation generated the correct interpretation. Interestingly the critical rationalist approach outperforms the purely empirical one.



