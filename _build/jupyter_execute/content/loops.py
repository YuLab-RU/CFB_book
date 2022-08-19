#!/usr/bin/env python
# coding: utf-8

# # Loops
# 
# ## Introduction to loops
# 
# A lot of computations involve processing a string one character at a time. Often they start at the beginning, select each character in turn, do something to it, and continue until the end. This pattern of processing is called a **traversal**. One way to write a traversal is with a `while` loop:
# 

# In[1]:


s ='GCTTGACAGGTAGACAGG'

index = 0
while index < len(s):
    base = s[index]
    print(base)
    index = index + 1


# This loop traverses the string (`s`) and displays each letter (`base`) on a line by itself. The loop condition is `index < len(s)`, so when index is equal to the length of the string, the condition is false, and the body of the loop is not executed. The last character accessed is the one with the index `len(s) - 1`, which is the last character in the string.
# 
# Both indexing and the function `len` also work on a `list`, so we could do the same if `s` were a `list`:
# 

# In[2]:


s = list(s)

index = 0
while index < len(s):
    base = s[index]
    print(base)
    index = index + 1


# We could do more interesting stuff on this sequence, for instance counting the number of different bases within the sequence:
# 

# In[3]:


index = 0
a = 0
c = 0
g = 0
t = 0
 
while index < len(s):
    base = s[index]
    if base == 'A':
        a = a + 1
    elif base == 'C':
        c = c + 1
    elif base == 'G':
        g = g + 1
    elif base == 'T':
        t = t + 1
    index = index + 1

print(a)
print(c)
print(g)
print(t)


# Please look carefully at this code to see what is done in each step!
# 
# 
# The `for` statement is another looping statement which iterates over a sequence of objects i.e. go through each item in a sequence. `for` works also works on a `list` and a `string`. Here are some examples:

# In[4]:


s ='GCTTGACA'
for i in s:
    print(i)


# In[5]:


cell_lines = ['HCT116', 'HeLa', 'HEK293']
for i in cell_lines:
    print(i)


# The `range()` function is convenient to create a sequence of integers, while you can specify the beginning, end and step-size of your integers. You can convert the result to a `list`. By default it starts at 0. For example:
# 

# In[6]:


range(5)


# In[7]:


list(range(0, 5))


# In[8]:


for i in range(0,5):
    print(i)


# In[9]:


for i in range(1, 10, 2):
    print(i)


# `range()` could help us to step through a sequence to get the indexes of the codon-starts one by one:
# 

# In[10]:


s = 'GCTTGACAGGTAGACAGGACCCATAGACAGGATAGACAGGTAGACAGGGATAGACAGGGATAGCCAGATAGACGATAGCGATGATAC'
for i in range(0, len(s), 3):
    print(i)


# So, we can now use this range of integers to step through the sequence (s), obtain the codons, append them to an empty list, and finally print the new list:
# 

# In[11]:


codons = []
for i in range(0, len(s), 3):
    codons.append(s[i:i + 3])
print(codons)


# Note how we used a `for` loop, `range`, `append`, and `list` slices !
# 
# ## Glossary of loop terms
# 
# * `while`
# * `for`
# * `if`
# * `elif`
# * `range`

# ## Exercises: loops
# 
# **Exercise 4.1**
# 
# Extend the following code so that it prints all items in the list `my_list` in consecutive order:
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# ```
# 
# **Exercise 4.2**
# 
# Study the following code and run it:
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# for idx in range(0, 5):
#     print(my_list[idx])
# ```
# 
# 1. Question: does this produce the same output as your final code for exercise 4.1?
# 2. Question: what is the output when you change `5` to  `3` in the second line (this changes the values passed to the `range()` function)?
# 3. Question: what is the output when you change `0` (the start of the range) to  `1` in the second line?
# 4. Question: what is the output when you change `5` to  `6` in the second line?
# 
# **Exercise 4.3**
# 
# Study the following code (do not run it yet):
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# for idx in range(0, 5):
#     print(my_list[idx])
#     print(my_list[idx])
# ```
#         
# 1. Question: how many lines are printed to the screen? Can you give the precise sequence? (Run the code to verify your answer)
# 
# Run this code:
# 
# ```python
# my_list = ['A','B','C','D','E']
# for idx in range(0, 5):
#     print(my_list[idx])
# print(my_list[idx])
# ```
# 
# 2. Question: how many lines are printed?
# 3. Question: why is *only* the last value printed twice?
# 
# Now consider this code:
# 
# ```python
# my_list = ['A' ,'B', 'C', 'D', 'E']
# for idx in range(0, 5):
#     print(my_list[idx])
# for idx in range(0, 5):
#     print(my_list[idx])
# ```
#         
# 4. Question: how many items are printed to the screen? Can you give the precise sequence? (Run the code to verify your answer)
# 5. Question: explain why the order is different from the first example in this exercise?
# 
# **Exercise 4.4**
# 
# Run the following code:
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# for idx in range(0, 5):
#     for second_idx in range(0, 2):
#         print(my_list[idx])
# ```
#         
# 1. Question: what is the output of this code?
# 2. Question: which of the examples from exercise 4.3 does it reproduce?
# 3. Question: What happens if you change the variable name `second_idx` to `my_second_idx`? Explain.
# 
# **Exercise 4.5**
# 
# Run the following code:
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# line_number = 0
# for idx in range(0, 5):
#     for second_idx in range(0, 2):
#         line_number = line_number + 1
#         print("line_number:", line_number, 
#             "index:", idx,
#             "item in list at this index:", my_list[idx],
#             "second_index:", second_idx)
# ```
#             
# 1. Question: what is the output of this code?
# 3. Question: What happens if you change the variable name `second_idx` to `my_second_idx`? Explain why the behaviour is different compared to exercise 4.4.3.
# 
# **Exercise 4.6**
# 
# Run the following code:
# 
# ```python
# my_list = ['A', 'B', 'C', 'D', 'E']
# for item in my_list:
#     print(item)
# ```
# 
# 1. Question: what is the output?
# 
# The following code produces the same output but uses a different variable name to iterate over the items in the list:
# 
# ```python
# my_list = ['A','B','C','D','E']
# for items in my_list:
#     print(items)
# ```
#         
# 2. Question: why does it make more sense to use the singular `item` than the plural `items` as the variable name in the for loop?
# 
# **Exercise 4.7**
# 
# Use two nested for loops and one print statement (so a maximum of three lines/statements) to produce the following output:
# 
#     1 1
#     1 2
#     1 3
#     1 4
#     2 1
#     2 2
#     2 3
#     2 4
#     3 1
#     3 2
#     3 3
#     3 4
#     4 1
#     4 2
#     4 3
#     4 4
# 
# **Exercise 4.8**
# 
# The goal of this exercise is to write Python code to print the longest open reading frame (ORF). For this exercise you can assume that the sequence is in the correct frame, you don't have to check all three frames! Note that generally the uracils (U) in mRNA sequences are represented by thymines (T).
# 
# Regard the following sequence (copy-paste):
# 
# ```python
# seq = """catattctggaggagcctcccctcctcatgccttcttgcctcttgtctcttagatttg\
# gtcgtattgggcgcctggtcaccagggctgcttttaactctggtaaagtggatattgttgccatcaat\
# gaccccttcattgacctcaactacatggtgagtgctacatggtgagccccaaagctggtgtgggagga\
# gccacctggctgatgggcagccccttcataccctcacgtattcccccaggtttacatgttccaatatg\
# attccacccatggcaaattccatggcaccgtcaaggctgagaacgggaagcttgtcatcaatggaaatc\
# ccatcaccatcttccaggagtgagtggaagacagaatggaagaaatgtgctttggggaggcaactagga\
# """
# ```
# 
# 1. Starting at the first base of the sequence, use a loop to step through the sequence to print the codons (steps of 3 bases) one by one. 
# 
# 2. Using a similar loop to print all positions that encode for a start or stop codon, and to print whether it is a start or a stop.
# 
# 3. Make two lists: `starts` and `stops`. Using a similar loop again, fill `starts` with all start positions, and fill `stops` with all stop positions.
# 
# 4. Which start and stop positions give the longest ORF?

# In[ ]:




