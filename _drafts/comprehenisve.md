## Notes from the Underground: Studying for my comprehensive exam

As part of the CS PhD program, students have to pass an oral exam after their first year. The exam is based on a literature review written (LINK) by the student on a field in Computer Science. Since it is related to my research, I chose to write about RNA structure prediction and classification. In order to prepare for the oral exam, I'm taking notes on all the papers I reviewed and figures I could post them in case anyone else was interested. 	

I will cover techniques for RNA 2D then 3D structure modelling, prediction, and classification. The format is like a cheat sheet as I want to retain the key pieces of information. For a more 'review' style treatment have a look at the literature review. (LINK)

When relevant I will outline the following information for each technique:

* Definition of the problem
* Justification (past results and shortcomings)
* Algorithm employed
* General properties of class of algorithm
* Time and space complexity
* Empirical performance (accuracy, etc.)
* Limitations and caveats



### RNA 2D Structure Prediction 

#### Nussinov Algorithm (1980) 

**Problem representation:**

We write a sequence $\omega$ as a word from the alphabet $\{\texttt{A, U, C, G\}}$. A secondary structure $s$ on $\omega$ is a set of pairs $(i, j)$ of indices in $\omega$ that obey the following rules:

* $i \neq j$ and each base can only pair with one other base
* $\omega_i\omega_j \in \{\texttt{AU}, \texttt{CG}, \texttt{GU}\}$
* Given other pair $(k, l)$ we have $i < k < l < j$ or $k < i < j < l$ $\rightarrow$ no pseudoknots
* $j - i < p$ for some integer $p$. Typically choose 3. Sets the minimum loop size.


**Previous approaches:** Identify all sets of valid helices (watson-crick pairing segments) and use approximate energy functions to find the minimum energy structure. This was very slow due to high number of combinations to consider and intractable on larger sequences.

**Goal:** compute maximally paired secondary structure for a given sequence.

**Approach:** 

* *Dynamic Programming (DP):*  optimization method used for problems with two key characteristics, *an optimal sub-structure* and *overlapping sub-problems*. The solution to DP problems can be computed by optimally solving smaller problems and storing the solution in a data structure (memoization). The algorithm iterates over the sub-problems such that at the current step it can look up the previously stored solutions to the smaller sub-problems instead of re-computing. 


**Algorithm:**

The Nussinov algorithm builds the maximally paired secondary structure. 

We define $OPT(i, j)$ to be a function that returns the maximum number of basepairs on the subsequence in the interval $[i, j]$. 

The problem is solved using DP and the following recursion:

$$ OPT(i, j) = \max \begin{cases}
\max_{k } OPT(i, k-1) + OPT(k+1, j-p) + 1 &\text{$j$ paired with}\\
														& \text{ $k \in [i, j-1]$}\\
OPT(i, j-1)  \ &\text{$j$ unpaired}
\end{cases}
$$

This recursion says that the maximum number of base pairs on a subsequence between $i$ and $j$ is the maximum of two cases. 

1. The base $j$ forms a pair with another base $k$ on the interval $[i, j-p]$. This gives us two optimal substructure $OPT(i, k-1)$ and $OPT(k+1, j-1)$ and we add 1 to count the formed base pair. At this iteration, the algorithm tests all possible values of $k$ to find the one with the maximum value.
2. There is no pairing $k$ with $j$ so we just compute the optimal solution on $OPT(i, j-1)$ 

*Optimal sub-structure*: We say that a problem has an optimal substructure if the optimal solution is a combination of optimal solutions to smaller problems. This decomposition is possible thanks to the fact that we don't allow any crossing interactions (pseudoknots) in the secondary structure. In this setting, any pair between two positions $(j, k)$ will form two substructures whose pairs are strictly nested within the basepair $(j, k)$ and so we can independently compute the optimal structure on the two sub-structures.

We also have the base case where $j - i < p$ so we know that it is impossible to have a base pair in that interval and so $OPT(i, j) = 0$. 

<!-- ![nussinov]({{ site.url  }}/assets/nussinov.png) -->
![nussinov](../assets/nussinov.png)

*Overlapping sub-problems:* DP performs best when computing the solution to a sub-structure, the algorithm has previously encountered and stored the solutions required for the current step. This is clearly the case for RNA structure since we can obtain $OPT(i, j)$ as a function of previously computed values $OPT(i, k-1)$, $OPT(k+1, j-1)$, and $OPT(i, j-1)$ by computing $OPT$ on intervals of increasing length. Therefore $OPT$ will actually be a matrix of size $N \times N$ that will store the computed values after each iteration.


Once the matrix is filled, we have the maximum number of base pairs on every sub-string of the sequence and $OPT(1, N)$ storing the score for the whole sequence. Obviously, this is not what we were looking for which is the secondary structure. To obtain the structure we perform what is known as a *backtracking* procedure to reconstruct the optimal structure. 

Optionally, one could store a pointer during the computation of $OPT$ that stores which case in the recursion was used at each step. Otherwise, this is how the backtracking works:

```python
backtrack(i, j):
	if j < i:
		return
	elif OPT[i][j] == OPT[i][j-1]:
		backtrack(i, j-1)
		return
	else:
		for k such that i < k < j-p and (i, k) complimentary:
			if OPT[i][j] == OPT[i][k-1] + OPT[k+1][j-1] + 1:
				print(k, j are paired)
				backtrack(i, k-1)
				backtrack(k+1, j-1)
				return
```
So we start from the whole sequence $OPT(1, N)$ and see if $j$ forms a pair. If $OPT(i, j) == OPT(i, j-1)$ it means that $j$ was not paired as the score remains the same. Otherwise we have to search for the $k$ that pairs with $j$ which we do inside a for loop. If we find that some $k$ explains the score at $OPT(i, j)$ then we print the pair $(j, k)$ and recurse to the two substructures formed by the pair.

**Complexity:**

* Filling the matrix: $\mathcal{O}(N^3)$
* Backtrack: $\mathcal{O}(N^2)$. If all bases unpaired then you fall into the second `if` each time and go through the sequence in $N$ steps. If at each step you have to look for a pair then at worst you go through each other position $N$ times to get $\mathcal{O}(N^2)$.
* Space: since we are simply filling a matrix and all computations are done on the same matrix storage is only $\mathcal{O}(N^2)$. 

**Limitations:** 

* No distinction between base pair types
* No consideration of stacking bases to stability or single stranded regions as de-stabilizing contributions.
* Consequently, Nussinov prediction does not yield very realistic structures.
* However, Nussinov also descrives a procedure for incorporating contextual information in the addition of base pairs as part of the backtracking. 

#### Zuker's Algorithm (1981)

The fundamental unit of the Nussinov algorithm is the base pair. However, experimentally derived energy values for RNA structure  are done on larger secondary structure units. More specifically on loops and stacks. Therefore, an algorithm that can leverage this information to identify a minimal free energy instead of a maximally paired structure stands to yield more accurate results.

**Problem Representation:*

Zuker defines the elementary unit of a secondary structure as a *face*. We think of RNA 2D structure as a planar graph where nodes are bases and edges are interactions connecting the bases. We then distinguish between two types of edges: external edges connect the backbone of the RNA, and internal edges connect a pair of bases. Finally, a *face* is a planar region bounded on all sides by edges. The image below shows two representations of an RNA structure with its faces labeled. 

![nussinov](../assets/faces.png)

We can see that a *hairpin* is a face with one internal edge. A stack is defined by two consecutive internal edges. Bulges and internal loops have two internal edges that are separated by one (bulge) or more (internal loop) exterior edges on one side. Bifurcation loops are faces with three or more interior edges. With the exception of the bifurctaion loop, the Zuker algorithm uses experimentally derived energy values for each of the types of faces.

**Approach:** DP

**Algorithm:** 

The Zuker algorithm is a somewhat slight modification of the Nussinov algorithm but dealing with faces instead of base pairs.

We define following terms:

* $W(i, j)$ is a DP table which contains the energy of the minimum energy structure on the interval $[i, j]$.
* $V(i, j)$ is a DP table contains the energy of the minimum energy structure on the interval $[i, j]$ where $(i, j)$ are paired.
* $E(F)$ is the energy of a given face. For example, if F is a stacking region we would have $E(F) = -1.8$ kcal/mol as this would be a stabilizing element.

The optimal energy will be stored in $W(1, N)$. Which can then be used to reconstruct the optimal structure using a similar backtracking procedure to the one used by Nussinov.

In order to fill the tables we apply the following recursions:


$$V(i, j) = min\{E1, E2, E3\}$$

Where

$$E1 = E(FH(i,j)) $$

$$E2 = \min_{i < i' < j' < j} \{E(FL(i, j, i', j')) + V(i', j')\} $$

$$E3 = \min_{i+1 < i' < j-2} \{W(i+1, i') + W(i'+1, j-1)\} $$

So for $V(i, j)$ we take the minimum over three possible cases. 

* $E1$ is a simple hairpin loop formed by a single interior loop $(i, j)$.
* $E2$ Is the structure with two interior edges $(i, j), (i', j')$ where $(i', j')$ is nested inside $(i, j)$. This can form a stack if the two internal edges are contiguous, or a bulge/interior loop if they are not. The recursion here scans through all valid $(i', j')$ and takes the minimum.
* In the case of $E3$, $(i, j)$ define a bifurcation and thus the formation of two independent substructures $W(i+1, i')$ and $W(i'+1, j-1)$. Remember $W(i,j)$ stores the energy of the optimal structure between $[i,j]$ regardless of whether $i$ and $j$ are paired.	

Now we have to fill $W$.

$$
W(i, j) = \min\{W(i+1, j), W(i, j-1), V(i, j), E4\}
$$

Where:

$$E4 = \min_{i < i' < j' < j} \{W(i, i') + W(i' +1 , j)\}$$


We consider three possibilities for $i$ and $j$: 

1. $i$ or $j$ are not paired with any other base. So we just take the value $W(i+1, j)$ or $W(i, j-1)$ respectively.
2. $i$ and $j$ are paired. We already computed this and find it in $V(i, j)$.
3. $i$ and $j$ are paired but not with each other but instead pair with nested bases $i'$ and $j'$ (s.t. $i < i' < j' < j$. We can then decompose this as $W(i, i') + W(i'+1, j) = W(i, j'-1) + W(j', j)$.

Finally, as with the Nussinov algorithm, we have the base case as the entries where $i$ and $j$ are too close to form any nested structures so their energy values can be read off directly without further computation.

**Complexity:** Time and space complexity are the same as for Nussinov.

**Limitations:** The main contribution of this algorithm was its ability to incorporate experimental and evolutionary information to the predictions which showed that this additional information was crucial to improving predictions. The main drawback is that Zuker's algorithm does not yield suboptimal structures. This was addressed later by other algorithms.


### RNA 2D Classification [DUE: MONDAY]

Zuker's algorithm demonstrated the importance of additional information to the prediction of accurate RNA secondary structures. One very important type of external information is evolutionary conservation. It is widely know that because non-coding RNA function is determined mainly by its structure, natural selection acts on the structure allowing the sequence to vary a fair amount. Therefore by comparing sequences of homologous RNAs we can see see that compensatory mutations emerge that preserve the RNA's structure. Knowing this, there arose a need for tools that were able to model the sequence variation in natural RNAs in a way that can be used to improve structural prediction and automatically build libraries of **RNA families** whose members share a common 2D structure.
 

#### Covariance Models (1994)

The most widely used framework for modelling RNA structural families is known as a Covariance Model and was simultaneously proposed in 1994 by Eddy and Rivas.

**Problem representation:** 

The main idea with CMs is to model structural families as *Stochastic Context Free Grammars (SCFGs).* Grammars were initially used by Noam Chomsky to model the rules that generate language. Applying this to RNA, we can think of an RNA structural family as a language, and all the sequences that belong to that family as words or sentences that can be produced from that grammar's rules.

In this context it is useful to think of RNAs as ordered binary tress.

![tree](../assets/tree.png)

The usual representation of an RNA 2D structure can be seen in A and its translation into a tree is shown in B. Each node represents a left or right singlet, a bifurcation or a base pairing. We can see that starting from the root of the tree and writing the sequence found in the node we can reconstruct the structure in A. 

More generally, can write the corresponding grammar rules for this kind of tree:

$$ S \rightarrow xSy  | xS | Sx | SS | \epsilon $$

These rules can be thought of as "rewriting rules". The upper case symbols are called "non-terminals" and lowercase symbols are called "terminals". Non-terminals are replaced by one of five the re-writing rules (above). When the sequence consists only of "terminals" then we are done. For example, we can re rewrite $S$ with one of the four possible re-writing rules. For example, $aSb$ replaces $S$ with a base $x, y \in \{A,U,C,G\}$ to the left and to the right forming a base pair. The $SS$ state implies a bifurcation in the structure as each non-terminal starts a new branch of the sequence. The $\epsilon$ state ends the string as it does not contain any non-terminal for further re-writing. 

If we wanted to write the structure above using these rules we would have a set of re-writings as follows:

$$\begin{align} S \implies aS \implies aS \implies S_1S_2 \\ 
&\implies S_1u \implies gS_1c \implies a S_1 u ... \epsilon \\
&\implies gS_2c \implies gS_2c \implies cS_1 ... \epsilon \end{align} $$

We can represent derivations like this using what is known as a 'parse tree'. (below)

![parse](../assets/parse.png)


This is a good representation of a single sequence and structure. However, an RNA family consists of multiple different sequences that belong to the same structure. Therefore we need to introduce some sequence variability and structural context information in the nodes of this tree. 

The way sequence variation is typically identified in bioinformatics is with a multiple sequence alignment (MSA). We can think of an MSA as a matrix $A$ where $A[i][j]$ is character $j$ of sequence $i$. The character set in an MSA contains the four bases and a special "gap" character written "-" which implies that character $j$ was deleted from the sequence with respect to the conserved consensus. Characters in each row of the matrix are arranged so that the entropy of each column $j$ is minimized and therefore conserved positions can be identified. So to model a family of RNAs we build a tree whose nodes capture the sequence variability in the MSA and the correlations in the secondary structure. Nodes can emit single bases, paired bases, insertions and deletions *with some probability* (hence, stochastic). As with the first example, a traversal of an SCFG generates members of the alignment in a probabilistic manner.

**Algorithm(s):**

There are three main challenges in dealing with SCFGs:

1. Given a CM and an observed sequence, how do the characters in the sequence align with the states of the CM? $\rightarrow$ alignment problem.
2. Given a CM and an observed sequence, what is the likelihood that the CM generates that sequence? $\rightarrow$ scoring problem.
3. Given a set of sequences and structures, what set of SCFG states and parameters best represents the sequences? $\rightarrow$ training problem.

*Alignment problem*

The task is to associate each nucleotide in a sequence $\omega$ with a state in the SCFG $\mathcal{G}$. 

Once again, we use our friend DP to break down the problem into smaller sub-problems and iteratively compute the full solution. In this case, we will want a DP table that contains the maximum likelihood of aligning $\mathcal{G}$ to the interval $[i, j]$. Additionally, we also need to compute most likely state $y \in M$ (given $M$ states) for an internal $[i, j]$. We can think of $y$ as the root of subgraph in the parse tree which covers $[i, j]$. This produces a 3 dimensional matrix $S_{i, j, y} \in \mathbb{R}^{N X N X M}$.

### RNA 3D Structure Prediction [DUE: TUESDAY]

#### `MC-Sym` (1991)

#### `RMDetect` (2011)

#### `JAR3D` (2015)

### RNA 3D Structure Classification [DUE: WEDNESDAY]

#### `RNA 3D Atlas` (2013)

#### `CaRNAval` (2016)
