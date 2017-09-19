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

We can always get the **type** or **class** of a piece of data with the `type(Object o)` function.

```python
>>> print(type("Pizza")
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
* `%` modulo operator, works on `int`
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

* `> < >= <= ==` are technically operations on numerical types but they yield a boolean. e.g. `5 <= 6` results in `True` `6 == 6` is also `True`



### String operations

### Mutability

### Using object Functions

### Exercises

## Conditional Statements



