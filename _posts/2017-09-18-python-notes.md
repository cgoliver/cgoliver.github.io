---
layout: post
title: "Letters to a young Python programmer"
date: 2017-09-18
comments: true
---

This is a collection of notes and exercises on the topics covered in COMP 364. The material here is by no means exhaustive and is simply meant as a reference and study aide. I will try my best to keep these notes up to date with the material as we cover it. Please feel free to leave comments at the bottom if anything is unclear.

## Data Types, Names, and Objects

Anything you can tell Python to remember in memory is what we call an **Object**. An object is simply a piece of information that Python stores in a box and gives it a label `ID`.

Every Object is **unique** and is thus given a unique identifier `id(object)`

You can assign **names** to objects using the `=` **operator**.

```python
larry = 5
```

Assigns the name *larry* to the *object* `5`. Now if I want to use the value of the object I can just use the name instead of its super complicated id which if i'm crazy I can get using `id(5)` or `id(larry)`.


The mapping of **names** to objects is called a **namespace**. You can give multiple names to the same object.

```python
samantha = 5
tamara = samantha
janelle = samantha
```

There are several kinds (eventually we will see this is actually infinite) of data you can tell Python to *remember* and to perform **operations** on. The ones that have been defined out of the box by Python are called the *built-in* data types. 

Here are some of the simplest ones:

* `int` e.g. `1, 2, 3, -500, 10000`
* `float` e.g. `0.1, 1.0, -129.992`
* `str` e.g `"my name is Margaret"`
* `bool` e.g. `True`, `False`

As we can see, each of these pieces of information is of a different **type** (aka **class**) and so each of them behaves differently.

We can always get the **type** or **class** of a piece of data with the `type(object)` function.

```python
>>> print(type("Pizza"))
<type 'str'>
```

This is how Python is able to know how to manipulate the different types of data. It says, "everything is an Object, and I can perform operations on Objects according to their kind."

> God made the wild animals according to their kinds, the livestock according to their kinds, and all the creatures that move along the ground according to their kinds. And God saw that it was good. (Genesis 1:25)

 
An **operation** is an action that the interpreter performs on *expressions* to yield a new *expression*. 

Depending on the **type** of Object we are dealing with, we can perform different kinds of *operations*.

Some examples:

```python
#this is an expression. 
5  
#this is also an expression built using the + and / operators
(5.0 + 4) / 5 
#this is NOT an expression
#no new value is yielded , we are just labeling an object.
#python evaluates the expression on the right
#and assigns a name to the resulting object
matthew = (5.0 + 4) / 5
```

### Operations on numbers
* `+ - * /` pretty straightforward. Work on `float` and `int`
* `%` modulo operator, works on `int` and returns the remainder of dividing the first number by the second.
* `+= -= /= *=` are are shorthand for `x = x + 1`, `x = x * 4` etc. They evaluate the expression on the right and assign it back to the same name. Example:

```python
#this
>>> x = 5
>>> x += 2 
7
# is equivalent to this
>>> x = 5
>>> x = x + 2
7
```

### Boolean operations

The `bool` data type can take on one of two values: `True` or `False`. Booleans are very useful when we are trying to make *decisions* with our program.

Operations (given `A` and `B` are `bool` expressions):

* `A and B` results in `True` if and only if `A` is `True` and `B` is `True`. 
* `A` or `B` results in `True` if one or both of `A` or `B` is `True` 

| `A`        | `B`           | `or`  | `and`
| ------------- |:-------------:| -----:| ----:|
| `True`      | `True` | `True` | `True`|
| `True`      | `False`     |   `True` | `False` |
| `False` | `True`      |    `True` | `False` |
| `False` | `False`      |    `False` | `False` |

* `> < >= <=` are technically operations on numerical types but they yield a boolean. e.g. `5 <= 6` results in `True` `6 == 6` is also `True`. 
* `==` checks two objects for equality of **value**. 
* `is` checks whether two objects are the same. i.e. have the same `id`.

```python
>>> s = "Juicy J"
>>> y = "Juicy J"
>>> id(s)
4353534928
>>> id(y)
4353535504
>>> s == y
True
>>> s is y
False
>>> y = s
>>> y is s
True
```
You will probably never use `is` but `==` is very useful.

### String operations

You can evaluate a slice of a string using indices. An *index* is like a counter that indicates the position of a character in a string.

This is the syntax for string slicing on some string `s`: `s[start:stop:step]`. The `stop` index is not included in the new string. The first index of a string is `0`.

Negative numbers for `start`, `stop`, `step`, mean "go from the end of the string towards the start.

Note that slicing the string gives you a new string and leaves the original string unaffected.

```python
>>> s = "Bad and Boujee"
#this will be a new string object
>>> bad = s[0:3] 
>>> print(bad)
"Bad"
#if you don't specify a stop index it goes till the end
>>> boujee = s[8:]
>>> print(boujee)
"Boujee"
#string from start to end skipping every other character
>>> skip = s[::2]
>>> print(skip)
'BdadBue'
>>> s[-1]
'e'
>>> s[-6:]
"Boujee"
# nice way to reverse a string. give a negative step.
# give me whole string and step in a negative direction
>>> s[::-1]
'eejuoB dna daB'
# go backwards stepping by 2 positions
>>> s[::-2]
'ejo n a'
# after all this, the original string is unaffected
# we were just creating new strings each time
>>> print(s)
"Bad and Boujee"
```

You can use `len(string)` to get the length of the string (i.e. number of characters. This returns an integer.

```python
>>> len(s)
14
```

You can stick two strings together. This is called **concatenation**. Concatenating two strings yields a **new string.** The `+` operator on strings concatenates.

```python
>>> first_name = "Taylor "
>>> last_name =  "Swift"
>>> full_name = first_name + last_name
>>> print(full_name)
"Taylor Swift"
# a shortcut using +=
# this creates a string by evaluating
# first_name + last+name
# and gives it the name first_name
>>> first_name += last_name
>>> print(first_name)
"Taylor Swift"
```

### Mutability

### Accessing object attributes

### Exercises

## Conditional Statements



