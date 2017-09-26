---
layout: post
title: "Letters to a young Python programmer"
date: 2017-09-18
comments: true
---

This is a collection of notes and exercises on the topics covered in [COMP 364](www.cs.mcgill.ca/~cgonza11/COMP_364). The material here is by no means exhaustive and is simply meant as a reference and study aide. I will try my best to keep these notes up to date with the material as we cover it. Please feel free to leave comments at the bottom if anything is unclear.

> There is nothing to writing. All you do is sit down at a typewriter and bleed. (Ernest Hemingway)

## Data Types, Names, and Objects

[reference](https://docs.python.org/3/reference/datamodel.html)

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
[reference](https://docs.python.org/3/library/stdtypes.html)

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
The same goes for numerical and boolean types. The data types we have seen until now are all immutable. The main advantage of immutability is that it makes objects easier to store and look up because Python can always assume they will take up the same amount of space in memory and have to be accessed in exactly the same way. Having immutable types also makes sense when we don't want the objects to change how they behave. We wouldn't want to change the meaning of the integers or boolean objects since it is likely to lead to nonesense.

The cost is that if we want to compute expressions with immutable objects, we have to essentially make copies and create new objects each time. See string example above. We'll see examples of *mutable* objects in the upcoming sections.

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

[reference](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

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
	y = "i am also in the function"
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
Functions can accept any number of arguments. Example..

```python
def add_five_numbers(a, b, c, d, e):
	result = a + b + c + d + e
	return result
x = add_five_numbers(1, 2, 3, 4, 5) 
print(x)
#prints 15
```

The `print()` function can take many arguments:

```python
>>> a = 4
>>> b = "bob"
>>> c = "steve"
>>> print(a, b, c)
4 bob steve
```
Note that the order in which you provide the arguments **matters**.

```python
def subtract(a, b):
	return a - b

print(subtract(1, 4))
#not the same as
print(subtract(4, 1))
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
[reference](https://docs.python.org/3/whatsnew/3.6.html#pep-498-formatted-string-literals)
	
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
>>> x = 5
>>> x_squared = square(x)
 
>>> msg_str = f"You gave me {x} and I got {x_squared}"

>>> msg_str = f"You gave me {x} and I got {x**x}"

>>> print(msg_str)
'You gave me 5 and I got 25'
 
 ```
 
 
### Exercises
1. Write a function called `repeat(s, n)` that takes a `str` object `s` and returns a string that is copied `n` times. Example: `repeat("hi ", 3)` should give `hi hi hi`.
2. Write a function called `suffix_reverse(s, n)` that takes as input a `str` object `s` and `int` object `n`. First, it prints a string that looks like this. `"You gave me the string 'We were living in Paris' and the number 5".` Then, it returns the last `n` characters of `s` in reverse order. (Hint: if you want to include quotation marks in a string, use the **escape character** `\`. 
e.g. 

```python
>>> s = "Plato said, \"Only the dead have seen the end of war \"."
>>> print(s)
>>> "Plato said, "Only the dead have seen the end of war"."
``` 
Escape characters tell Python to treat the next character differently. In this case it tells Python to include the next `"` in the string and not treat it as the beginning of a new string.


## Conditional Statements
[reference](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

When you write your code in a `.py` file and give it to the interpreter it executes one line at a time from the top of the file until it reaches the bottom. What if we want our program to behave differently depending on some conditions? More specifically, what if we want certain parts of the code to execute only if some condition is true? This amounts to endowing python programs with the ability to make _decisions_.


To to this, we introduce the **if** statement. A **statement** in python is a line of code that does not produce a new object or modifies any values. Instead, it gives the interpreter some directions on how to execute the program. Think of statements as road signs. 

We've already seen the name binding statement `x = 5` which binds the name `x` to the object `5`. Here python isn't computing any new values or performing any operations, it's just an instruction so the interpreter remembers a name for you.

Ok, back to the **if** statement. Let me just give an example.

```python
x = 5
y = 2
if x > y == True:
	print("x is bigger")
print("done")
```

This is what the interpreter does as it reads from top to bottom:

1. Bind the name `x` to the object `5`
2. Bind the name `y` to the object `2`
3. Evaluate expression after `if`. If result is `True` execute code that is indented. Otherwise, skip indented code.
4. Execute print statement.

So now we have some code whose execution *depends* on something else. Here it depends on the value of `x` and `y`. Try setting `x=2` and `y=5` and see what happens. You should see that the line `print("x is bigger")` never gets reached.

**Syntax**: To write an `if` statement you use the key word `if` followed by a **boolean** expression which evaluates to either `True` or `False` and you end the line with a colon `:`. Anything you want python to execute if the condition evaluates to `True` you place one tab in.

What if you have several cases that you want to test? Use the `elif` statement (short for "else if").

```python
x = 10
y = 8
if x > y:
	print("x is bigger")
elif x < y:
	print("x is smaller")
else:
	print("x and y are equal")
```

You can have as many `elif` in a row. It is not necessary that they end with an `else` statement but it is usually good practice to deal with an `else` case. Python goes through the conditions one at a time. As soon as it encounters the first `True` condition it executes its code and skips the rest of the cases. So the order of your statements can sometimes be important.

```python
jon = "Stark"
tyrion = "Lannister"

if len(jon) == len(tyrion):
	print("same length")
elif jon[2] == tyrion[1]:
	print("both a")
elif jon[1] == tyron[-3]:
	print("both t")
else:
	print("hello")
```
In this case, both `elif` blocks evaluate to `True` but only the first one will actually execute since python skips the rest as soon as it finds one that is `True`.

If none of the `if` or `elif` statements evaluated to `True` then the `else` block will execute. You can also use an `else` after an `if` block.

In the `jon` and `tyrion` example, if you wanted both `elif` blocks to execute you could put them both in `if` statements.

```python
if jon[2] == tyrion[1]:
	print("both a")
if jon[1] == tyrion[-3]:
	print("both t")
```
Here, both print calls will execute as they belong to independent `if` statements. 

### Exercises

1. Write a function called `xor(a, b)` that takes two `bool` objects and returns `True` only if **one** of a or b is true and `False` otherwise.
2. Write a function called `is_palindrome(s)` that takes one string `s`and returns `True` if `s` is palindromes, i.e. it reads the same forwards and backwards.

## Containers: Lists, Tuples, and Sets
[reference](https://docs.python.org/3/tutorial/datastructures.html)

Until now we have been dealing with individual objects, each floating around in memory on their own. We've been binding individual `str` or `bool` objects to names and performing operations of them.

However, the world is full of collections of things: the days of the week, genes in a genome, grades in a class, names of past lovers, petals on a flower, etc. We would like to be able to have some kind of *container* for these things that lets us work with them efficiently. 

So python has some more built-in types that we can use as containers for other objects. The main ones are lists, tuples, and sets.

### Lists: the mutable container

This is how you store an empty list object

```python
mylist = []
```
This is how you store a list with some stuff already in it.

```python
stuff = ["pencil", "books", "calculator", "phone"]
#is much better than
thing1 = "pencil"
thing2 = "books"
thing3 = "calculator"
thing4 = "phone"
```

If you want to access one of the things in the list, you just use its name and tell python which position in the list you want to access.

```python
>>> print(stuff[1])
"books"
```

You can use exactly the same kind of indexing and slicing as with strings (see above).

```python
>>> print(stuff[1::2])
['books', 'phone']
```

Lists are **mutable** which means we can modify the value of a list object. A useful example is the *attribute* of the `list` type, `list.append(object)`. This function adds an object to the end of the list, essentially modifying the value of the list.

```python
>>> id(stuff)
4339084744
>>> stuff.append("laptop")
>>> print(stuff)
["pencil", "books", "calculator", "phone", "laptop"]
#same id, same object. different value
>>> id(stuff)
4339084744 
>>> stuff[0] = "binder"
#lists can hold objects of different types.
stuff.append(3000)
```
Since lists are objects and lists hold objects, it follows that lists can hold other lists. This kind of construction is often useful in many programming problems. In math, we often work with matrices which in Python can be thought of as lists of lists. 

```python
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```
This represents a matrix that looks like this:

$$
mat = 
\begin{bmatrix}
1 & 2 & 3\\ 
4 & 5 & 6 \\
7 & 8 & 9 
\end{bmatrix}
$$

Each list in the list `mat` would represent one of the rows in the matrix.

Let's say we want to change the $6$ to a $0$.

```python
mat[1][2] = 0
```
Why does this work?

```python
>>> print(mat[1])
[4, 5, 0]
>>> print(mat[1][2]
0
```

We can ask Python if a certain value is stored in a list using the `in` keyword.

```python
>>> mylist = [1, 2, 3, 4]
>>> 4 in mylist
True
>>> 0 in mylist
False
# The in keyword only checks one level of nesting.
>>> mymat = [[1, 2, 3], [4, 5, 6]]
>>> 3 in mylist
False
>>> [1, 2, 3] in mylist
True
>>> 3 in mylist[0]
True
```
### Tuples: the immutable container

A tuple can hold the same kinds of objects as a list. The only difference is that tuples are **immutable**. For this reason, they are often used to store things that you don't want to change, and whose index you want to *always* represent the same thing. 

Let's say I wanted to keep track of the student ID of each person in the class. Since people can add or drop the class,  I would probably want to keep that information in a list cause it's easy to grow or shrink a list. Okay so I have a list where each element is a student's info. Now how should I fill that list? Let's say I only ever care about the student's name and their McGill ID. These things don't change. So I'm tempted to use a tuple. So my code would look something like this.

```python
>>> students = [("John", 260452134), ("Mary", 2601502135), ("Rose", 2001202933)]
```

That's a list of tuples. Let's say a new student joins the class.

```python
>>> students.append(("Tracy", 2601002231)) 
```
and now the list has one more tuple representing the student "Tracy"'s info.

Because the tuples are immutable I know that the name string will always be at index 0 and the ID will be at index 1 of a particular tuple. 

So let's say I want the ID of the most recently added student, I would just do

```python
>>> most_recent = students[-1][1] #this will be the ID number.
```

Because lists can grow and shrink we can't be sure that the index will always hold the same kind of information.

Tuples also have the advantage of being faster to access and more memory efficient. Because the size of a tuple is fixed, Python can know exactly how much memory it needs to reserve for that tuple. On the other hand, a list can always grow so python may often have to over-compensate in case you decide to make the list bigger.

Just to make sure, let's try to modify a tuple and see what happens.

```python
>>> mytup = ("Carlos", 5558116519)
>>> mytup[0] = "Dante"
TypeError: 'tuple' object does not support item assignment
```
Naturally, we can understand that there is no `append()` function for tuples.

However, if a tuple contains a mutable object, we *can* modify that.

```python
>>> tuptup = ([1, 2, 3], "Hello")
>>> tuptup[0].append(4)
>>> print(tuptup)
([1, 2, 3, 4], "Hello")
```

### Sets: the container for unique things

The other major container in Python is the set. Sets work like math sets if you've studied them. In a set, every element is **unique**, and the elements are **unordered**. Having this kind of guarantee is often useful as you try to solve more and more problems. Along with this container, Python provides some very useful functions which implement set operations. Some examples will clarify all this.

A recap on how to initialize the containers:

```python
mylist = [1, 2, 3] 
mytup = (1, 2, 3)
mset = {1, 2, 3} #note empty set is set() not {}
```
You can store a set with the curly braces.

## Loops

Now that we have containers with a bunch of things in them. We want to be able to quickly perform operations on them. This is where loops come in. Loops are simply a way to repeat a set of python commands a certain number of times. This saves you from a lot of copy pasting of the same code.

The simplest loop is the `while` loop. Loops are `statements` like the `if` statement. They don't make any operations on their own, they just tell the interpreter how to execute your code.

Here is an example of the simplest possible loop:

```python
while True:
	print(""" This life as you now live it and have lived it,
	 you will have to live once more and innumerable times 
	 more; and there will be nothing new in it, 
	 but every pain and every joy and every thought and sigh
	 and everything unutterably small or great in your life
	 will have to return to you, all in the same succession
	 and sequence - even this spider and this moonlight
	 between the trees, and even this moment and I myself. 
	 The eternal hourglass of existence is turned
	 upside down again and again, and you with it, 
	 speck of dust!""")
```

When python encounters the `while` statement it evaluates the boolean expression to its right. If it sees a statement that is `True` and enters the loop body (one tab in) and executes the code inside it. Once it has marched through the code in the loop body it **goes back to the `while` statement** and evaluates the boolean expression to its right. If it sees something that is `True` it goes back into the loop body and executes again and goes back to the top and repeats. In this example, that loop will never stop executing since the condition never changes and we will have Nietzche's quote repeated forever. This is called an **infinite loop** and you generally want to avoid them.

Here's an example of a `while` loop that does terminate.

```python
x = 100
while x > 0:
	print("The original is unfaithful to the translation.")
	x = x - 1

```

Here are the steps the interpreter takes:

1. Bind `x` to `100`
2. Evaluate boolean expression `100 > 0` result is `True`.
3. Continue inside loop body
4. Print Jorge Luis Borges quote
5. Evaluate expression `x-1` get value of `99` and bind it to name `x`
6. Go back to `while` statement and evaluate `99 > 0` this is `True`.
7. Repeat
8. When `x=0` the `while` condition will be `False` and the interpreter will skip the loop body.

### List and Set Comprehensions

## Functions

### Why use functions?

### The anatomy of a function

### The `return` statement

### Namespaces + Functions

Functions define their own local namespace. 

> In that book which is my memory,
On the first page of the chapter that is the day when I first met you,
Appear the words, ‘Here begins a new life’. (Dante Alighieri, Vita Nuova)
