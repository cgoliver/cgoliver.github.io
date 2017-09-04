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



### RNA 2D Structure Prediction [DUE: SUNDAY]


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

#### Zuker Algorithm (1981)

The fundamental unit of the Nussinov algorithm is the base pair. However, experimentally derived energy values for RNA structure  are done on larger secondary structure units. More specifically on loops and stacks. Therefore, an algorithm that can leverage this information to identify a minimal free energy instead of a maximally paired structure stands to yield more accurate results.

**Problem Represntation:*

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

$$E4 = \min_{i < i' < j' < j} \{W(i, i') + W(i' +1 , j\}$$


We consider three possibilities for $i$ and $j$: 

1. $i$ or $j$ are not paired with any other base. So we just take the value $W(i+1, j)$ or $W(i, j-1)$ respectively.
2. $i$ and $j$ are paired. We already computed this and find it in $V(i, j)$.
3. $i$ and $j$ are paired but not with each other but instead pair with nested bases $i'$ and $j'$ (s.t. $i < i' < j' < j$. We can then decompose this as $W(i, i') + W(i'+1, j) = W(i, j'-1) + W(j', j)$.

Finally, as with the Nussinov algorithm, we have the base case as the entries where $i$ and $j$ are too close to form any nested structures so their energy values can be read off directly without further computation.

**Complexity:** Time and space complexity are the same as for Nussinov.

**Limitations:** The main contribution of this algorithm was its ability to incorporate experimental and evolutionary information to the predictions which showed that this additional information was crucial to improving predictions. The main drawback is that Zuker's algorithm does not yield suboptimal structures. This was addressed later by other algorithms.


### RNA 2D Classification [DUE: MONDAY]

#### Covariance Models


### RNA 3D Structure Prediction [DUE: TUESDAY]

#### `MC-Sym` (1991)

#### `RMDetect` (2011)

#### `JAR3D` (2015)

### RNA 3D Structure Classification [DUE: WEDNESDAY]

#### `RNA 3D Atlas` (2013)

#### `CaRNAval` (2016)
