---

layout: post
title: LaTeX Image Grids
date: 2018-08-15
comments: true 
---

# Generating Grids of Images in LaTeX with datatool and tikz

This is a quick one but I thought it would be worth sharing as it took me quite a bit of digging to find all the tools I needed to get what I wanted done.

### Problem: 

I wanted to generate grids of related images on various pages from PDF files. Since I was having trouble getting matplotlib to embed PDFs instead of PNGs I figured I'd give LaTeX a shot.

Note: this is an artificial example, I don't actually make pdfs of paintings. It was easier to get fun jpgs for this example but it works just as well with PDFs.

`artists.csv`:

```
artist-picasso,artist-monet,artist-nolde
artist-raphael,artist-leonardo,artist-michelangelo

```

[Here]({{ site.url }}/assets/artists.pdf) is an example of the resulting PDF.


For each artist name, I have a folder containing their self-portrait `/portraits` and `/examples` with an example of their paintings in the format `{artist_name}.jpg`. 

For each row in the CSV, I want to make a page in the document with a column for each artist containing their portrait and an example of their paintings.

The full code is below and I will briefly outline some of the main components and tools I found useful, of course there is much more available than what I will discuss.

## datatool

[datatool](https://www.ctan.org/pkg/datatool) is really nice for reading, looking up, and iterating through tabular data files. 

### Loading database

* `\DTLsetseparator{,}` pretty self-explanatory, tells the package which character to use to separate the columns.


* `\DTLloaddb[noheader]{artists}{artists.csv}` loads the file `artists.csv` into the macro `artists`. I used the option `noheader` to tell it my CSV does not have a header row with column labels. Columns are then given the default names `Column1, Column2,` etc.

### Looping over rows

* `\DTLforeach{artists}{}{loop body}` iterates over the rows of the CSV. Since I don't care about the column names here, the second argument is left empty. But you can use it to assign macros to column names. Say we have a header column `a,b,c` we can assign commands to them as:

* `DTLforeach{artists}{\adam=a, \bob=b, \charlie=c}` so now we can access columns by name.`

* Also useful, the iteration index in the for-loop is stored in `\DTLcurrentindex`.

### Looping over rows

* `\DTLforeachkeyinrow{\artist}{loop body}` loops over the columns in the current row. Must be used inside a row `\DTLforeach`. Assigns the value of the current row to the first argument, in this case, `artist`. 
* You can also get the current index of the column in `\dtlcol`.

FYI there are a lot more useful tools in the documentation such as conditionals `\DTLiffirstrow` which let you treat specific rows specially.

## xstring

I also needed to do some string splitting to build paths to the appropriate files so I used the `xstring` package.

* `\StrSplit{string to split}{position}{left}{right}` this command splits the first argument at the position in the second argument and stores the left part and right part in the last two arguments. 

## Checking for existence of file

Some of the files I was going to include would sometimes be absent and I wanted a way to handle this case without crashing the compilation. Thankfully latex has a nice conditional to help.

* `\IfFileExists{filename}{true-branch}{false-branch}` so I can include the graphics in the true branch and do nothing or put a placeholder in the flase branch.

## tikz 

This is a very well-known package so I don't think I need to go into too much detail here but I simply placed each graphic as a node to form a grid with the following syntax:

`\node (name) at (0, 0) {\includegraphics{pic.pdf}};`

In order to properly position the images in a grid, I used the column index `\dtlcol` and a constant factor to select a row in my image grid.

I also wanted to get rid of any padding around the images which is accomplished with the following arguments when creating the `tikz` picture:

`\begin{tikzpicture}[every node/.style={inner sep=0,outer sep=0}]`

Of course, I could have used `subfig` or `subcaption` packages but I wanted to use tikz in case I wanted any additional drawing on the immages such as frames and arrows.

## Miscellaneous command line tools

In the process, I also learned about two very nice BASH tools. 

* My file list CSV contained underscores which `datatools` and after reading underscores in filenames are not good practice, I decided to rename my files containing dashes to underscores. For this, I used a bash find and replace with a for loop:

`$ for x in `ls`; do mv $x ${x//_/-}; done`

The syntax is `${variable//find/replace}`.

* Another cool one I didn't know about is `basename` which returns the basename of a path:

```
$ basename /path/to/file.txt
$ file.txt
```

* When generating my images there was a long list of files I had to process with a bash script which was taking some time. So I discovered the GNU command `parallel` [docs](https://www.gnu.org/software/parallel/parallel_tutorial.html) which on Mac does not come default but is a quick `brew install parallel` away and is really cool. 

The basic usage is:

```
$ cat filelist.txt | parallel script.sh -in {} -out {./}.out
```

Here `filelist.txt` contains a list of files we need to process and sends each line to `script.sh` and `parallel` takes care of launching each call in a different process. The `{}` are called string replacements which we can use to manipulate the format of the input. For example `{./}` strips the file suffix so we can make the output suffix be `.out`.

## Full code

```latex
\documentclass{article}
\usepackage[margin=0.2in]{geometry}
\usepackage{tikz}
\usepackage{datatool}
\usepackage{xstring}
\usepackage{pdflscape}

\begin{document}

\DTLsetseparator{,}

\DTLloaddb[noheader]{artistgroups}{artists.csv}

\DTLforeach{artistgroups}{}{
			\begin{landscape}
			\begin{tikzpicture}[every node/.style={inner sep=0,outer sep=0}]
			\DTLforeachkeyinrow{\artist}{
				\DTLcurrentindex
				%get the ligand name
				\StrSplit{\artist}{7}{\a}{\name}
								% name
					\node () at (6*\dtlcol-5,0) {{\Large \name}};
				% portrait, leaving a space after the macro allows parser to end macro nicely.
				\IfFileExists{portraits/\name .jpg}{
					% portrait
					\node () at (6*\dtlcol-5 ,5) {\includegraphics[width=0.2\textwidth]{portraits/\name .jpg}};}
					{missing}
%					% painting
				\IfFileExists{examples/\name .jpg}{
					\node () at (6*\dtlcol-5,15) {\includegraphics[width=0.2\textwidth]{examples/\name .jpg}};}
					{missing}
			}
			\end{tikzpicture}
			\end{landscape}
			\clearpage
	}

\end{document}  
```

Of course, I am open to suggestions for better ways to approach this problem!