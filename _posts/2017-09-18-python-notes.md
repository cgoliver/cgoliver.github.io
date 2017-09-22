---
layout: post
title: "Letters to a young Python programmer"
date: 2017-09-18
comments: true
---

This is a collection of notes and exercises on the topics covered in COMP 364. The material here is by no means exhaustive and is simply meant as a reference and study aide. I will try my best to keep these notes up to date with the material as we cover it. Please feel free to leave comments at the bottom if anything is unclear.

## Data Types, Names, and Objects

Anything you can tell Python to remember in memory is what we call an **Object**. An object is simply a piece of information that Python stores in a box and gives it a label `ID`.

Every Object is **unique** is given a unique identifier `id(object)`

You can assign **names** to objects using the `=` **operator**.
 

```python
larry = 5
```

Assigns the name *larry* to the *object* `5`. Now if I want to use the value of the object I can just use the name instead of its super complicated id which if i'm crazy I can get using `id(5)` or `id(larry)`.


The mapping of **names** to objects is called a **namespace**. You can give multiple names to the same object.

In Python we have *things* (objects) and *names* for things. Think of people (objects) wearing name stickers. The **namespace** is like the party they're all attending. We can swap around people's names (like removing and sticking on nametags) but the people themselves stay the same. 

```python
#gives the object '5' the name samantha
>>> samantha = 5
#now the object 5 has 2 names: samantha, tamara
#python puts another sticker that says 'tamara' on 5
>>> tamara = samantha
>>> print(samantha, tamara)
5 5
# now I create the object 500 give it a sticker that says samantha
>>> samantha = 500
# this has no effect on the object '5' samantha used to point to
>>> print(tamara)
5
```


There are several kinds (eventually we will see this is actually infinite) of data (objects) you can tell Python to *remember* and to perform **operations** on. The ones that have been defined out of the box by Python are called the *built-in* data types. 

Here are some of the simplest ones:

* `int` e.g. `1, 2, 3, -500, 10000`
* `float` e.g. `0.1, 1.0, -129.992`
* `str` e.g `"my name is Margaret"`
* `bool` e.g. `True`, `False`
* `NoneType` e.g. `None` empty data.

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
# you can also multiply strings!
>>> s * 2
'Bad and BoujeeBad and Boujee'
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

Some objects in Python you are allowed to modify, and others you are not allowed to modify. This is known as mutability (can modify) and immutability (cannot modify). Strings are immutable. You can give different names to the same string, but you can never modify the contents of the object.

```python
s = "Justin"
s[0] = "j" # ERROR
```
The same goes for numerical and boolean types. The data types we have seen until now are all immutable. The main advantage of immutability is that it makes objects easier to store and look up because Python can always assume they will take up the same amount of space in memory and have to be accessed in exactly the same way. The cost is that if we want to compute expressions with immutable objects, we have to essentially make copies and create new objects each time. See string example above.

### Accessing object attributes

We saw that objects are pieces of data that behave according to their kind. What this means is that they have a specific set of **attributes** that are shared among all objects of a certain type. **attributes** are just other objects that belong to each object. So a specific person (object) of type human (class) can have various attributes which themselves are objects with names. For example, the person can have an attribute called `'height'` which is a `float` with some value. Different people will have different values but they will all have as an attribute the `height` object. 

We can access an object's attributes using the `.` operator followed by the name of the attribute we want to access.

The `dir(object)` function prints out a list of all the attributes of a given object or class.

```python
>>> dir(int)
>>> ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
```
All of these are names to objects that can be accessed for any instance of the `int` class. So if I store a specific `int` object I should expect the same result from `dir()`

```python
>>> x = 300
>>> dir(x)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
```
Okay so that's good we get the same list of *attributes*. Let's see what happens when we try to access one of them.
	
```python
>>> x = 300
>>> x.bit_length() #more on the brackets later
9 # number of bits to store this number
```
This is a good point to introduce functions. We'll get back to accessing object attributes in a bit.

### Quick intro to functions

Python is not very fun without functions so let's give you a little intro so we can talk about more interesting things. I will go into more detail in a later section.

You can think of a function as a box that performs some task given some input and produces some output. 

In Python terms, it is a block of python code that executes when you *call* it. When you call it you can determine how it will run. 

You can write your own functions to do whatever you want. Here's the syntax for defining a basic function.

```python
def function_name(function_input):
	#some code
	
	return #some value
```

Essentially, you are storing an object and giving it a name just like when we did `x=4` except function objects are more complex so they need more work to define. Functions are objects that contain code that executes when you call them.


Functions are used when you write code that can be re-used and you don't necessarily want to re-write the code each time you want to accomplish some task. Let's write a function that squares a number.

```python
def square(x):
	return x*x
```

What this is saying is, take the value of what is in the round brackets, do some operations to it and return it. **Python knows which operations belong to the function by taking everything that is indented once to the right.**

```python


def some_function():
	#this indented code will only run if some_function() is called
	s = "hello i am in the function"
	y = "i am also in the function
	#also in function
	print(s + y)
	
print("i am outside the function definition")
# removing the call below will cause the program to not
# print the code in some_function() when executing
some_function()
```

The `return` keyword is what spits out the output of the function (an object or a name). You can choose whatever you want for the `return`. Obviously whatever makes most sense is preferable. Now we can use our `square()` function to square any number and we only had to write the code to do it once.

```python
>>> x = 5
>>> x_squared = square(x)
>>> print(x_squared)
25
>>> square(12)
144
```
As you can see, calling a function is as simple as writing its name and including the **arguments** (a.k.a) input in round brackets. 

Since functions are also objects...

```python
>>> id(square)
4303247792
```

... they can also be used as class or object attributes.


For example, the `__cmp__` attribute is a function tells the `==` operator how to compare two `int` objects.

```python
>>> x = 20
>>> y = 25
>>> x.__cmp__(y)
-1 #-1 here means x < y
>>> y = x
>>> x.__cmp(y)
0 #means both values are equal
```
**Important note:** when functions are accessed as attributes of an object (with the `.` operator) the function **also** receives the object before the `.` as input. So in the `x.__cmp(y)__` call, **both** `x` and `y` are available to the function.

**Very important note:** `return` is *NOT* the same as `print()`. Calling the `print()` function simply **displays** text to the screen. It does not produce an object that you can store in memory and do operations on. Example..

```python
def square(x):
	return x*x
num = 5
#stores the result of the square() function
sq = square(num)
#you can display the result later
print(sq)
#displays 25 to the screen but you can't do anything with
#the value later.
print(x*x)

```

This is all I will say about functions for the moment. We will go into more details later.

## String functions

Now that we have a better idea of what functions are, we can have a look at functions available to us by default in Python that let us work on the data types we have seen.

I'll just put a bunch of examples in the code block below. You can always look them up in the [documentation](https://docs.python.org/3/library/stdtypes.html). 

```python
>>> s = "Shake it off.    "
>>> s_clean = s.strip()
>>> print(s_clean)
"Shake it off."
>>> print(s)
"Shake it off.    "
>>> s.replace("off", "on")
"Shake it on.    "
>>> print(s)
"Shake it off.    "
>>> len(s_clean) #length of the string
17
>>> s_clean.upper()
"SHAKE IT OFF."
```

Sometimes you want to include some information that you computed into a string to print to the user. Say you have a function that squares a number and you want to display a nice message to the user saying "you asked me to square [number] and the result is [number squared]". This is called **string formatting**. There is a very useful function in Python that lets you do this. It's called `format()` and it is an attribute of the `str` class.

```python
def square(x):
	return x*x

x = 5
x_squared = square(x)

#all of the following are equivalent.

msg_str = "You gave me {0} and I got {1}".format(x, x_squared)

msg_str = "You gave me {} and I got {}".format(x, x_squared)

msg_str = "You gave me {adam} and I got {eve}".format(adam=x, eve=x_squared)

```
 
 Good news! In Python 3.6 we get a brand new feature which makes this even easier! It's called the **f-string**. All you have to do is put an `f` before the string quotes and python will automatically know that you want to format that string (without having to call the `format()` function). And it will use the names that are already in the `namespace` without having to pass them as input to the `format(name1, name2)` function. You can even evaluate Python expressions *inside* the string! Example:
 
 ```python
x = 5
x_squared = square(x)
 
msg_str = f"You gave me {x} and I got {x_squared}"

msg_str = f"You gave me {x} and I got {x**x}"
 
 ```
 
 
### Exercises
1. Write a function called `repeat(s, n)` that takes a `str` object `s` and returns a string that is copied `n` times. Example: `repeat("hi ", 3)` should give `hi hi hi`.
2. Write a function called `suffix_reverse(s, n)` that takes as input a `str` object `s` and `int` object `n`. First, it prints a string that looks like this. `"You gave me the string 'We were living in Paris' and the number 5".` Then, it returns the last `n` characters of `s` in reverse order. (Hint: if you want to include quotation marks in a string, use the **escape character** `\`. 
e.g. 

```python
>>> s = "Plato said, \"Only the dead have seen the end of war \".".
>>> print(s)
>>> "Plato said, "Only the dead have seen the end of war"."
``` 
Escape characters tell Python to treat the next character differently. In this case it tells Python to include the next `"` in the string and not treat it as the beginning of a new string.


## Conditional Statements

### Exercises

1. Write a function called `xor(a, b)` that takes two `bool` objects and returns `True` only if **one** of a or b is true and `False` otherwise.
2. Write a function called `is_palindrome(s, z)` that takes two strings `s` and `z` and returns `True` if `s` and `z` are palindromes, i.e. they read the same forwards and backwards.

## Lists and Tuples

## Loops



