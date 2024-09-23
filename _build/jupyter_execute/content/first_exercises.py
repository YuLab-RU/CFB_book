#!/usr/bin/env python
# coding: utf-8

# # First exercises
# 
# ## Exercises: integer (int) and string (str) variables
# 
# **Exercise 1.1**
# 
# Consider the following code:
# 
# ```python
# a = 10
# b = 4
# c = a + b
# print(c)
# ```
# 
# 1. Question: What is the value of `c` that is printed?
# 2. Modify the value that is assigned to variable `b` in such a way that the value of `c` printed to screen is `16`. 
# 

# **Exercise 1.2**
# 
# Create two variables `a` and `b`, and assign them the values 4 and 20 respectively. Create a new variable `c` that is the sum of these two variables. Your code should produce the following output by printing the value of the variable `c` to the screen:
# 
# ```python
# a + b = 24
# ```

# **Exercise 1.3**
# 
# Run the following code:
#     
# ```python
# a = 10
# b = 4
# c = a + b
# print(c)
# print(c)
# ```
# 
# 1. Question: Which value is printed to the screen and how often?
# 
# Now assign the variable `b` a new value after having printed the value of `c`, like so:
#     
# ```python
# a = 10
# b = 4
# c = a + b
# print('a + b = ',c)
# b = 10
# print('a + b = ',c)
# ```
# 
# 2. Question: Why does the value of the variable `c` not change between the first and the second print statement (in line 4 and line 6 respectively)?
# 

# 
# **Exercise 1.4**
# 
# Run the following code (make sure to write it *exactly* as shown here):
# 
# ```python
# a = '10'
# b = '4'
# c = a + b
# print(c)
# ```
# 
# 1. Question: what is printed to the screen?
# 2. Question: what type of variable are `a`, `b` and `c`? (e.g. list, integer, float, string)
# 3. Question: why does it not print `14` to the screen? You could also try this example to see what is happening:
# 
# ```python
# a = '10'
# b = '4'
# c = a + '+' + b
# print(c)
# ```

# **Exercise 1.5**
# 
# Have a look at the following code (do not run it yet):
# 
# ```python
# a = 10
# b = '4'
# c = a + b
# print(c)
# ```
# 
# 1. Question: what type of variable is `a`?
# 2. Question: what type of variable is `b`? 
# 3. Question: what is the output of the code? (Run it!)
# 4. Question: do you understand the output?

# ## Working with strings

# As you have seen, you can combine strings using the `+` operator.

# In[1]:


first_part = "this is "
second_part = "a long string"

print(first_part + second_part)


# If you want to access specific parts of a string you can use `[` and `]` with a number in between.

# In[2]:


msg = "hello there!"
msg[1]


# You'll see that `[1]` selects the second character of the string `"hello there!"`. Why the second and not the first? This is because Python, like many other programming language, starts counting at `0`.
# 
# There is a more extended version, where you create a *slice*. In this case you specify `[start:end]`. This looks as follows:

# In[4]:


msg[0:5]


# Here you see that you can take a *substring* of `string`. In other words, you select a smaller part of a `string`.
# 
# You can convert a number, such as an `int` or `float` to a string with the `str()` method.

# In[5]:


a = 0.12
print(type(a))
b = str(a)
print(type(b))


# Similarly, you can convert a string that contains a number to an integer with the `int()` function or to a float with the `float()` function.
# 
# Strings have a number of methods that allow you to perform a variety of useful functions. For instance, `lower()` creates a new string where all characters are in lowercase.
# 

# In[4]:


s1 = "ATG"
s2 = s1.lower()
print(s2)


# Similarly, you can use `upper()` to convert a string to all uppercase. These methods create a *new* string, they leave the string you use to call the method unchanged.
# 
# Here is a list of useful string methods. For a complete overview you can check the [Python string documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).
# 
# * `upper()` - Returns a string in uppercase
# * `lower()` - Returns a string in lowercase
# * `len()` - Returns the length of a string
# * `count()` - Returns the number of occurrences of a string within another string
# * `replace()` - Returns a string with specific text replaced 
# * `find()` - Return the first position where a substring is found, or -1 if is not found
# * `strip()` - Returns a string with all leading and trailing whitespace removed
# 

# ## Exercises: strings
# 
# **Exercise 1.6**
# 
# You are going to analyze the following sequence in more detail using Python:
# 
# ```
# GCTTGACAGGTAGACAGGACCCATAGACAGGATAGACAGGTAGACAGGGATAGACAGGGATAGCCAGATAGACGATAGCGATGATAC
# ```
# 
# To get this sequence into python you are allowed to copy paste!
# Provide answers + code to the following questions:
# 
# 1. What is the length of this sequence?
# 
# 2. What is the 40th base of this sequence?
# 
# 3. Is there a C in the sequence starting at base position 44 and ending at position 53? (let Python tell you)
# 

# **Exercise 1.7**
# 
# Given the following input:
# 
# ```python
# seq1 = "ATG"
# seq2 = "GATTACA"
# seq3 = "A"
# ```
# 
# Write the code that will calculate the total length of these three sequences and print the following output:
# 
# ```python
# Total length: 11
# ```

# **Exercise 1.8**
# 
# An open reading frame is a sequence of DNA that starts with the start codon ATG and ends with a stop codon (TAA, TAG or TGA). Take the following DNA sequence.
# 
# ```python
# dna = "TTGCATGTCAATCGATCGGATTGGTTGATTTATCCCGA"
# ```
# 
# This sequence contains one ORF, with a start codon at the 5th position and a stop codon (TGA) at the 26th position.
# 
# 1. Write code that will print the ORF of this sequence. 
# 
# Let's look at a different DNA sequence:
# 
# ```python
# dna2 = "CCGGTATGCGGTTCTGACCA"
# ```
# 
# 2. Does the code that you wrote for 1) also work for this sequence? If not, write code that will print the ORF of a DNA sequence (only with the TGA stop codon) that works with either of these sequences.
# 

# **Exercise 1.9**
# 
# Write code that will print the GC content of a sequence. This is the fraction of a sequence that is either C or G. When you use string `dna` from **1.8** it should print the following:
# 
# ```
# GC content: 42%
# ```

# **Exercise 1.10**
# 
# Write code that will print a sequence in lower-case with the ORF (start ATG, stop TGA) in upper-case.
# 
# For instance, the following sequence:
# 
# ```python
# dna = "TTGCATGTCAATCGATCGGATTGGTTGATTTATCCCGA"
# ```
# 
# Would be printed like this:
# 
# ```python
# ttgcATGTCAATCGATCGGATTGGTTGAtttatcccga
# ```
