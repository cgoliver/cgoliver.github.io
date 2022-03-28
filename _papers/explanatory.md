---

layout: page
title: Explanatory Learning, Beyond Empricism in Neural Networks 
topic: Machine Learning 

---

Authors: Mariani et al.

Date: 2022 

[paper](https://arxiv.org/pdf/2201.10222.pdf)

The authors develop a playground for this concept using simple geometric shapes on a fixed-size array. We can observe instances of a phenomenon as arrangements of shapes on the array. 

![]({{site.url}}/assets/el.png)

Arrangements that follow a common 'rule' are said to belong to the same phenomenon. In the example below, the rule/explanation is 'at least one square at the right of a red pyramid'. Here, the phenomeon is the set of all arrangements following this rule. An interpreter is a function that takes an explanation and an arrangement and decides whether or not it belongs to the phenomenon. Since this phenomeon is explainable (we just gave its explanation) we know that evaluating the interpreter on the all possible arrangements will give us the whole set of occurrences of this phenomenon.

The authors define several problems using this framework where we can be given multiple phenomena, explanations to some phenomena and not others, and partial sets of observations for said phenomena. The goal is usually to train a model that can accept an obeservation and determine whether it belongs to a given phenomenon, and going futher be able to generate explanations that satisfy an interpreter. 

Different approaches to this problem hint at debates in epistemology. For example, an approach that only works with occurrences and directly tries to map them to a correct interpretation would be called fully empirical since it assumes that all necessary knowledge can be derived from observations (i.e. data). Whereas a 'rationalist' approach tries to generate explanations before seeing the observations, and these observations are tested on data and updated. The authors formaize the rationalist approach in terms of deep learning architectures as 'Critical Rationalist Networks'. These models are built on language transformer models which generate English sentences as possible explanations which are fed to a decoder that determines whether the explanation generated the correct interpretation. Interestingly the critical rationalist approach outperforms the purely empirical one.
