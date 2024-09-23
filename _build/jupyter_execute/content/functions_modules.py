#!/usr/bin/env python
# coding: utf-8

# # Functions and modules
# 
# ## Functions
# 
# Functions are reusable pieces of programs. They allow you to give a name to a block of statements,
# allowing you to run that block using the specified name anywhere in your program and any number of
# times. This is known as *calling* the function. We have already used many built-in functions such
# as `print()`, `len()` and `range()`.
# 
# The function concept is probably *the* most important building block of any non-trivial software
# (in any programming language), so we will explore various aspects of functions in this chapter.
# 
# Functions are defined using the `def` keyword. After this keyword comes an *identifier* name for
# the function, followed by a pair of parentheses which may enclose some names of variables, and by
# the final colon that ends the line. Next follows the block of statements that are part of this
# function. An example will show that this is actually very simple.
# Here we define a function called `print_nuc_count()` using the syntax as explained above. 
# Run the example to see the output.
# 
# Example:

# In[1]:


def print_nuc_count():
    dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAG"

    for n in "ACGT":
        print(n, dna.count(n))
    print()

print_nuc_count()
print_nuc_count()


# Notice that we can call the same function twice which means we do not have to write the same code
# again.
# 
# ### Function Parameters
# 
# The function `print_nuc_count` as defined above takes no arguments.
# Therefore, there are no parameters declared in the parentheses in the function definition.
# Often, we want to supply some information to the function in the form of arguments, 
# so that the function can *do* something utilising those values.
# In that case we specify parameters in the function definition.
# These are basically just variable names that define the input to the function 
# so that we can pass in different values to it and get back corresponding results.
# The values of these variables are defined when we call the function and are already assigned values
# when the function runs.
# Parameters are specified within the pair of parentheses in the function definition, separated by
# commas. When we call the function, we supply the arguments in the same way.  
# 
# > **The difference between arguments and parameters**
# >
# > Note the terminology used - 
# > the names given in the function definition are called *parameters* 
# > whereas the values you supply in the function call are called *arguments*.
# 
# The function we defined above is not very useful. 
# We usually don't want to count the number of nucleotides in the same sequence again and again. 
# We will define a function that takes one argument, called `seq`, which is used to determine the number of nucleotides.

# In[2]:


def print_nuc_count(seq):

    for n in "ACGT":
        print(n, seq.count(n))
    print()

print_nuc_count("ACCGGGTTT")

dna = "GACTGGATAGAGTAG"
print_nuc_count(dna)


# **How It Works** 
# 
# The first time we call the function `print_nuc_count`, 
# we directly supply the sequence as arguments. 
# In the second case, we call the function with a variable as argument. 
# `print_nuc_count(dna)` causes the value of argument `dna` to be assigned to parameter `seq`. The `print_nuc_count` function works the same way in both cases.
# 
# 
# 
# ### Local Variables
# 
# When you declare variables inside a function definition, they are not related in any way to other
# variables with the same names used outside the function - i.e. variable names are *local* to the
# function. This is called the *scope* of the variable. All variables have the scope of the block
# they are declared in starting from the point of definition of the name.
# 

# In[3]:


x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


# **How It Works** 
# 
# The first time that we print the *value* of the name *x* with the first line in the function's
# body, Python uses the value of the parameter declared in the main block, above the function
# definition.
# 
# Next, we assign the value `2` to `x`. The name `x` is local to our function.  So, when we change
# the value of `x` in the function, the `x` defined in the main block remains unaffected.
# 
# With the last `print` statement, we display the value of `x` as defined in the main block, thereby
# confirming that it is actually unaffected by the local assignment within the previously called
# function.
# 
# 
# ### Default Argument Values
# 
# For some functions, you may want to make some parameters *optional* and use default values in case
# the user does not want to provide values for them. This is done with the help of default argument
# values. You can specify default argument values for parameters by appending to the parameter name
# in the function definition the assignment operator (`=`) followed by the default value.
# 
# Note that the default argument value should be a constant.

# In[4]:


def say(message, times=1):
    print(message * times)

say('Hello')
say('World', 5)


# **How It Works**
# 
# The function named `say` is used to print a string as many times as specified. If we don't supply a
# value, then by default, the string is printed just once. We achieve this by specifying a default
# argument value of `1` to the parameter `times`.
# 
# In the first usage of `say`, we supply only the string and it prints the string once. In the second
# usage of `say`, we supply both the string and an argument `5` stating that we want to *say* the
# string message 5 times.
# 
# > **Caution**
# > 
# > Only those parameters which are at the end of the parameter list can be given default argument
# > values i.e. you cannot have a parameter with a default argument value preceding a parameter without
# > a default argument value in the function's parameter list.
# >
# > This is because the values are assigned to the parameters by position. 
# > For example, `def func(a, b=5)` is valid, but `def func(a=5, b)` is *not valid*.
# 
# ### Keyword Arguments
# 
# If you have some functions with many parameters and you want to specify only some of them, then you
# can give values for such parameters by naming them - this is called *keyword arguments* - we use
# the name (keyword) instead of the position (which we have been using all along) to specify the
# arguments to the function.
# 
# There are two advantages - one, using the function is easier since we do not need to worry about
# the order of the arguments. Two, we can give values to only those parameters to which we want to,
# provided that the other parameters have default argument values.
# 

# In[5]:


def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)


# **How It Works** 
# 
# The function named `func` has one parameter without a default argument value, followed by two
# parameters with default argument values.
# 
# In the first usage, `func(3, 7)`, the parameter `a` gets the value `3`, the parameter `b` gets the
# value `7` and `c` gets the default value of `10`.
# 
# In the second usage `func(25, c=24)`, the variable `a` gets the value of 25 due to the position of
# the argument. Then, the parameter `c` gets the value of `24` due to naming i.e. keyword
# arguments. The variable `b` gets the default value of `5`.
# 
# In the third usage `func(c=50, a=100)`, we use keyword arguments for all specified values. Notice
# that we are specifying the value for parameter `c` before that for `a` even though `a` is defined
# before `c` in the function definition.
# 
# ### The `return` statement
# 
# The `return` statement is used to *return* from a function i.e. break out of the function. We can
# optionally *return a value* from the function as well.
# 

# In[6]:


def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))


# **How It Works**
# 
# The `maximum` function returns the maximum of the parameters, in this case the numbers supplied to
# the function. It uses a simple `if..else` statement to find the greater value and then *returns*
# that value.
# 
# Note that a `return` statement without a value is equivalent to `return None`. `None` is a special
# type in Python that represents nothingness. For example, it is used to indicate that a variable has
# no value if it has a value of `None`.
# 
# Every function implicitly contains a `return None` statement at the end unless you have written
# your own `return` statement. You can see this by running `print(some_function())` where the function
# `some_function` does not use the `return` statement such as:
# 

# In[7]:


def some_function():
    pass

print(some_function())


# The `pass` statement is used in Python to indicate an empty block of statements.
# 
# ```{note}
# There is a built-in function called `max()` that already implements the 'find maximum'
# functionality, so use this built-in function whenever possible.
# ```
# 
# 
# ## DocStrings - documenting your functions
# 
# Python has a nifty feature called *documentation strings*, 
# usually referred to by its shorter name *docstrings*. 
# DocStrings are an important tool that you should make use of since it helps to
# document the program better and makes it easier to understand. 
# We can even get the docstring back from, 
# say a function, when the program is actually running!
# 

# In[8]:


# Please note the function below is not optimal. In practise, we would 
# write the function to return a dictionary. Nevertheless, let us use 
# this example to illustrate the use of DocStrings.

def count_nuc(dna):
    """Returns the nucleotide content of a sequence.

    Arguments:
    dna -- a string of DNA sequence that should contain only "ACGT" characters.
    Return:
    a -- count of A's in the DNA sequence
    c -- count of C's in the DNA sequence
    g -- count of G's
    t -- count of T's
    """
    # Initialize empty variables
    a = 0
    c = 0
    g = 0
    t = 0

    for nuc in dna.lower():
        if nuc == "a":
            a += 1
        elif nuc == "c":
            c += 1
        elif nuc == "g":
            g += 1
        elif nuc == "t":
            t += 1

    return a, c, g, t

print(count_nuc("GATTACA"))
print()
print("Help:")
print(count_nuc.__doc__)


# **How It Works**
# 
# A string on the first logical line of a function is the *docstring* for that function.
# The convention followed for a docstring is a multi-line string where the first line starts with a
# capital letter and ends with a dot. Then the second line is blank followed by any detailed
# explanation starting from the third line. You are *strongly advised* to follow this convention for
# all your docstrings for all your non-trivial functions.
# 
# We can access the docstring of the `count_nuc` function using the `__doc__` (notice the *double
# underscores*) attribute (name belonging to) of the function.
#  
# If you have used `help()` in Python, then you have already seen the
# usage of docstrings! What it does is just fetch the `__doc__`
# attribute of that function and displays it in a neat manner for
# you. You can try it out on the function above - just include `help(count_nuc)` in your
# program. Remember to press the `q` key to exit `help`.
# 
# Automated tools can retrieve the documentation from your program in this manner. 
# Therefore, we *strongly recommend* that you use docstrings for any non-trivial function that you write. 
# The `pydoc` command that comes with your Python distribution works similarly to `help()` using docstrings.
# 
# ```{note}
# From now on, for this course, **all** your functions have to be documented using a docstring! 
# ```

# ## Exercises
# 
# **Exercise 6.1**
# 
# Write a function called `median()` that takes a list of numbers as an argument and returns the median as a `float`.  
# 
# <details>
# <summary> If you are struggling with this exercise, click on the triangle to view tips. </summary>
# 
# To start off, do not code anything yet. Just think along with the following questions.
# 
# 1. What is the definition of a median? If you don't know, see definition [here](https://en.wikipedia.org/wiki/Median).
# 2. If you are given the following list: `[1,3,20]`, what is the median? If you are given a different list: `[1,5,12,38]`, what is the median? 
# 3. What did you do differently for the two lists above? Why?
# 4. If I give you a new list, but you don't know how many items (individual numbers) it contains. What would you need to do?
# 5. In the two example lists in above, the numbers are given in order (lowest to highest). What would you do if they are not ordered?
# 6. Now collect your answers from parts 1-5. Write down the steps you would take to calculate the median, if you are given an unknown list of numbers. This is your *approach*. 
#    
#    ```{note}
#    The approach is the most important part of programming! If you do not have a solid approach, your code would never work in a consistent way. So really spend the time to develop and evaluate your approach before you start to code.
#    ```
# 
# 7.  Read the exercise again. Does your approach satisfy everything that the exercise is asking for? If it doesn't, modify your approach.
# 
# Once you have a good approach, you may start to code. Do it one step at a time. After writing the code for a step, do a small test and use `print()` to check that the output is correct. 
# 
# For example, if one of your steps is to "put the list in order (smallest to highest)", maybe you decide to use `list.sort()` to do this. But is it working as intended? To check this, make up a small list which is randomly ordered, run it through your code, then use `print()` to see if this has successfully put your list of numbers in order.
# 
# If you have been following these tips, then maybe you just wrote some code, but they are not in a function. Review the textbook materials from this chapter, and convert your code into a function. Then, you can test your function with some test lists. For example, if you run the following code:
# 
# ```python
# test_list_1 = [41, 149, 176, 63, 79, 43, 174, 148, 34, 25, 138, 99, 39, 32, 119, 113, 175, 182, 168, 80, 100, 16, 125, 59, 67]
# test_list_2 = [36, 170, 199, 17, 14, 21, 19, 105, 47, 175]
# print(median(test_list_1))
# print(median(test_list_2))
# ```
# your output should be:
# ```python
# 99.0
# 41.5
# ```
# 
# </details>
# 
# <br/>
# 
# 
# **Exercise 6.2**
# 
# Write a function called `sequence_type()` that takes one argument, a `string`. The function should return a `string` with one of three values: `"dna"`, `"protein"` or `"other"`. This should depend on the input. If the input only contains A, C, T, G or N it should return `"dna"`. If the input contains only valid one-letter IUPAC amino acid code (see IUPAC table below) it should return `"protein"`. In all other cases it should return `"other"`. The function should work, regardless of the input being upper-case, lower-case or a mix.
# 
# ```{note}
# Theoretically, a sequencing consisting of A, C, G, T, or N can be an amino acid sequence consisting of Alanines, Cysteines, Glycines, Threonines, and Asparagines. However, you can ignore this possibility for this exercise.
# ```
# 
# ```
# One-letter Code:  Three-letter Code:  Amino Acid:
# ----------------  ------------------  -----------
# A.................Ala.................Alanine
# B.................Asx.................Aspartic acid or Asparagine
# C.................Cys.................Cysteine
# D.................Asp.................Aspartic Acid
# E.................Glu.................Glutamic Acid
# F.................Phe.................Phenylalanine
# G.................Gly.................Glycine
# H.................His.................Histidine
# I.................Ile.................Isoleucine
# K.................Lys.................Lysine
# L.................Leu.................Leucine
# M.................Met.................Methionine
# N.................Asn.................Asparagine
# P.................Pro.................Proline
# Q.................Gln.................Glutamine
# R.................Arg.................Arginine
# S.................Ser.................Serine
# T.................Thr.................Threonine
# V.................Val.................Valine
# W.................Trp.................Tryptophan
# X.................Xaa.................Any amino acid
# Y.................Tyr.................Tyrosine
# Z.................Glx.................Glutamine or Glutamic acid
# ```
# 
# <details>
# <summary> If you are struggling with this exercise, click on the triangle to view tips. </summary>
# 
#    <details>
#    <summary>I. Problem analysis. </summary>
# 
#    1. Read the first sentence of the exercise. What is a function? What is an argument? This sentence specifies that the argument should be a `string`. What is a `string`? Can you think of some examples for a `string`?
#    2. Read the second sentence. What does 'return' mean? What is a 'value'? 
#    3. Both the first sentence and the second sentence talk about `string`s. Are they referring to the same thing? Why or why not? 
#    4. From the second sentence, you know that your function should return one of three possibilities. What are they? Keep them in mind as we continue analyzing the exercise.
#    5. Continue reading the text of the exercise. The 4th sentence states:
#       
#       >  If the input only contains A, C, T, G or N it should return `"dna"`.
# 
#       As you know, a DNA sequence is made up of only 4 nucleotide bases: A, C, T, or G. Why is 'N' included in the above sentences? What does 'N' mean? Think of an example `string` that is a sequence for `dna`, and write this down.
#    6. Continue reading the text of the exercise. The next sentence states:
# 
#       > If the input contains only valid one-letter IUPAC amino acid code (see IUPAC table below) it should return `"protein"`. 
# 
#       Look at the IUPAC table that is given to you. What information does this table contain? What does the code 'B' symolize? What does 'D' symbolize? What does 'N' symbolize? What does 'X' symbolize? 
# 
#       The sentence refers to *valid* one-letter IUPAC amino acid code. What is an *invalid* one-letter IUPAC amino acid code? Can you find an example?
# 
#       Think of an example `string` that is a sequence for `"protein"`, and write this down. 
# 
#    7. Continue reading the text of the exercise. Think of an example `string` for `"other"`, and write this down.
#    8. Read the last sentence of the exercise. Now look at your 3 example `string`s. Are your example `string`s all upper-case, all lower-case, or a mix? Modify some of these `string`s so you have an example of each.
#    9. Read the note that is part of the exercise. What does this mean? If you have the following `string`:
#       
#       ```python
#       'AcgNT'
#       ```
# 
#       What should your function return? What other option are you ignoring (as instructed by the note)?
#    
#    </details>
# 
#    <details>
#    <summary>II. Approach and code. </summary>
#    
#    1. Consider the 3 example `string`s that you have written down. What differentiates between them? In other words, what makes one of them a `dna`, one of them a `protein`, and one of them `other`? Write this down in three "if... then..." statements. This is the first draft of your *approach*.
#    2. It is important to critically examine your approach, and modify it if necessary. Consider the following 5 examples. Use your "if... then..." statements to determine if they are `dna`, `protein`, or `other`.
#       
#          ```python
#          str_1 = 'acgt'
#          str_2 = 'acgtd'
#          str_3 = 'acgtdj'
#          str_4 = 'AnApple'
#          str_5 = 'An Apple'
#          ```
#    3. Remember that in programming, you are basically giving instructions one step at a time. This means that the order of the steps is very important. Examine your three "if... then..." statements. Is the order of the three statement logical? If not, fix the order. You may also need to modify your "if... then..." statements.
#    4. Did you notice that it is very important to know what letters are symbols for nucleotides, and what letters are symbols for amino acids? Why is this? Let's collect the nucleotides and amino acids into two lists.
#         
#          ```python
#          nucleotide_list = ['a', 'c', 'g', 't', 'n']
#          aa_modified_list = ['b', 'd', 'e', 'f', 'h', 'i', 'k', 'l', 'm', 'p', 'q', 'r', 's', 'v', 'w', 'x', 'y', 'z']
#          ```
#    5. Notice that in the two lists above, we are placing the letters 'a', 'c', 'g', 't', and 'n' *only* in `nucleotide_list`, but *not* in the `aa_modified_list` (this is why we called this list the 'aa modified list', instead of just 'amino acid list'). Why are we doing this? How will it help us later?   
#    6. Next, recall what you've learned about the `in` operator in Chapter 2. For example, if you want to ask whether the letter `j` is in `nucleotide_list`, how would you code this? If you want to ask whether the letter `j` is in `aa_modified_list`, how would you code this?
#    7. Recall what you've leared about loops in Chapter 4. If you want to consider each individual letter in a string (e.g. `acgtdj`), one at a time, how would you code this? Combine this with your code from the previous step: consider the letters in a string one at a time, and for each letter ask whether it is in `nucleotide_list` and whether it is in `aa_modified_list`. 
#    8. Recall what you've learned about conditionals in Chapter 3. How can you use conditionals to convert your "if... then..." statements into code? Combine this with your code from the previous step.
#    9. Test what you have written with the three examples that you have written down in the previous section, and with the 5 examples given above. Did your code correctly classify each example into `dna`, `protein`, or `other`? If not, what went wrong? Isolate the issue and examine the logic behind your approach. Review what you have learned in previous chapters, and critically examine your code for any errors.
# 
#    </details>
# 
# 
#    <details>
#    <summary>III. Final touches and testing.</summary>
# 
#    If you have not done so already, convert your code into a function. Read the complete text of the exercise again. Does your code satisfy everything that the exercise asks for? 
#    
#    You can now test your function with the following code:
# 
#    ```python
#    test_str_1 = "FNEFDKRYAQGKGFITMALNSCHTSSLPTPEDKEQAQQTHHEVLMSLILGLLRSWNDPL"
#    test_str_2 = "FNEFDKRYAQGKGFITMALNSCHTSSLPTPEDKEQAQJQTHHEVLMSLILGLLRSWNDPL"
#    test_str_3 = "tgacctcaactacatggtgagtgctacatggtgagccccaaagctggtgtggg"
#    print(sequence_type(test_str_1))
#    print(sequence_type(test_str_2))
#    print(sequence_type(test_str_3))
#    ```
#    your output should be:
#    ```python
#    protein
#    other
#    dna
#    ```
#    </details>
# 
# </details>
# 
# <br/>

# ## Modules
# 
# Python functions can be stored together in a *module*. A module, a collection of functions with a certain theme, can be *imported* by another program to make use of its functionality. This is how we can
# use the Python standard library as well. First, we will see how to use the standard library
# modules.

# In[9]:


import math

print(math.sqrt(16))


# **How It Works**
# 
# First, we *import* the `math` module using the `import` statement. Basically, this translates to us
# telling Python that we want to use this module. The `math` module contains mathematical functionality. 
# 
# When Python executes the `import math` statement, it looks for the `math` module. In this case, it is
# one of the built-in modules, and hence Python knows where to find it.
# 
# If it was not a compiled module i.e. a module written in Python, then the Python interpreter will
# search for it in the directories listed in its `sys.path` variable. If the module is found, then
# the statements in the body of that module are run and the module is made *available* for you
# to use. Note that the initialization is done only the *first* time that we import a module.
# 
# The `sqrt()` function in the `sys` module is accessed using the dotted notation i.e. `sys.sqrt()`. It
# clearly indicates that this name is part of the `sys` module. Another advantage of this approach is
# that the name does not clash with any `sqrt` variable used in your program.
# 
# There are many more functions defined in the `math` module.

# In[10]:


print(math.pow(2, 5))
print()

result = math.log(2.71828183)
print(result)
print(math.isclose(result, 1))


# All the functions in the module are described [here](https://docs.python.org/3/library/math.html).

# ### The from ... import statement
# 
# If you want to directly import the `sqrt` function into your program 
# (to avoid typing the `math.`everytime for it), 
# then you can use the `from math import sqrt` statement.
# 
# In general, the `import` statement is better since your program will avoid name clashes and will be more readable.
# 

# In[11]:


from math import sqrt
print("Square root of 16 is", sqrt(16))


# ### Multiple imports
# 
# You can import from many different modules.

# In[12]:


import random
from datetime import date
from math import sqrt

n = 16
print("The square root of {} is {}".format(n, sqrt(n)))
print()

print("Today is {}".format(date.today()))
print()

print("Here you have a pseudo-random number:", random.random())
print("Or a random integer between 0 and 10:", random.randint(0, 10))


#  ```{note}
# In this book, we use the `import` statements in the cells where they're needed. However, in general, imports are **always** put at the **top** of the file.
#  ```

# ## Exercises
# 
# **Exercise 6.3**
# 
# Write a function `random_sequence()` that generates a string with a random DNA sequence of length `length`. The `length` argument should have a default value of `100`. All nucleotides should have an equal chance of occurring.
# 
# **Exercise 6.4**
# 
# Adapt your function `random_sequence()` and add an optional argument `gc`, which controls the total percentage of G + C in the random sequence that the function generates. This means that if you call `random_sequence(length=100, gc=40)` that 40 out of the 100 characters of the returned string should be a G or a C. The default GC% should be 50%. Note that there are multiple solutions possible. 
# 
# Hint: check the following functions from the `random` module:
# 
# * `randint()`
# * `random()`
# * `choice()`
# * `shuffle()`
# 

# In[ ]:




