---

layout: page
title: "Research Group"
nav: true
order: 1
permalink: /research

---

This is regarding the direction of my project research group the Max Planck Institute for Biochemistry.

---

So much depends upon the structure of protein and RNA. 

The 3D spatial arrangement (geometry/structure) of biomolecules dictates what kinds of physical interactions are favorable and therefore which biological functions are accessible to DNA/RNA/proteins. 
Finding exactly which geometrical patterns within these molecules are the ones we should pay attention to is a needle in the haystack problem.
In this group, we take the data-driven approach.
That is, we build **scalable structure-aware** algorithms that process the growing datasets of biological structures to identify patterns which influence function.
A clear understanding of the patterns that mediate structure to function relationships will help uncover new biological mechanisms and point towards solutions to pathologies.

Here are some active projects.

## Deep learning on protein structures

We recently developed [ProteinShake](https://proteinshake.ai) which allows deep learning practitioners easy asccess to impactful biological tasks on proteins. (Accepted at NeurIPS 2023)
 
![](/assets/shake_tasks.png)

 
## Representation learning on RNA 3D networks

RNA structures adopt complex folds by forming base pairs, we have developed unsupervised learning methods which have proven useful in [drug discovery](https://academic.oup.com/nar/article/48/14/7690/5870337) and [network motif mining](https://academic.oup.com/bioinformatics/article/38/4/970/6428528) applications. Through [rnaglib](https://academic.oup.com/bioinformatics/article/38/5/1458/6462185) we hope to explore more applications.

![](/assets/rna_pre.png)

## Graph pattern mining

Structural patterns adopted by molecules are often dynamic and noisy, making traditional graph pattern mining algorithms less appropriate. [MotiFiesta](https://arxiv.org/abs/2206.01008) captures approximate network patterns in any graph dataset while at the same time serving as pre-training for classification models.

![](/assets/motifiesta.png)

# Open Positions

If you find this interesting, we are looking for a highly motivated **PhD student** to work at the intersection of structural biology, deep learning and pattern mining on graphs. ([posting]({{site.url}}/assets/phd_search.pdf))([submit application](https://recruitingapp-5446.de.umantis.com/VacanciesIntraxData/452/Application/New/2))

Please contact me for more info: oliver@biochem.mpg.de
