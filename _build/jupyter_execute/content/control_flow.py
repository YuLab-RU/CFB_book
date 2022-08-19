#!/usr/bin/env python
# coding: utf-8

# # Control flow
# 
# ## Introduction to control flow
# 
# The `if` statement is used to **check a condition**: if the condition is true, we run a block of statements (called the if-block), next we can test another condition (`elif`, short for "else if") and we process another block of statements (called the elif-block). Lastly, we can use an `else` clause, which is optional.
# 

# In[1]:


cell_lines = ['HCT116', 'HeLa', 'HEK293']
c = 'HeLa'

if c in cell_lines:
    # New block starts here
    print('Yes, cell line is present.')
    # New block ends here
elif c not in cell_lines:
    # Another block
    print('No, not present')
    # block ends here


# Now, run the same commands for `c = 'U2Os'`.
# 

# Note the following:
# 
# * In the example above we used `if c in cell_lines` to test a condition ("is c an element of the `list` cell_lines?").
# * The checked condition statement is always followed by `:`.
# * The following block is **indented**, **4 spaces** is conventionally used.
# * The outcome of such test is `True` or `False`. If `True`, the codeblock is executed
# * Here are some operators for condition tests:
#     * `in` is an element of
#     * `==` equivalence (values, strings)
#     * `>`  greater than
#     * `>=` greater than or equal
#     * `<`  less than
#     * `<=` less than or equal
#     * `!=` not equal
# * You can combine condition tests with `or`, `and`
# * You can "invert" a condition by placing `not` in front
# * `=` is different from `==` !!
# 
# 
# Here is another example, in this case we use `if` to compare values:

# In[2]:


some_number = 10
n = 9
 
if n < some_number:
    print('Your number n is less.')
elif n == some_number:
    print('Your number n is exactly the same!')
else:
    print('No idea...greater maybe?')


# Run the same block for other values of `n`.
# 
# 
# The result of your condition test is `True` or `False`. Check this by running:
#     
#     c in cell_lines
# 
#     n < some_number

# So, simply running the following also works:
# 

# In[3]:


if True:
    print('Yes, no doubt about this...')


# One conditional can also be nested within another. For example:
# 

# In[4]:


x = 5
y = 6

if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')


# Although the indentation of the statements makes the structure apparent, nested conditionals become difficult to read very quickly. 
# **Logical operators** (e.g. `and`, `or`) often provide a way to simplify nested conditional statements. For example, we can rewrite the following code using a single conditional:
# 

# In[5]:


x = 1

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number.')


# The `print()` statement is executed only if we make it past both conditionals, so we can get the same effect with the and operator:
# 

# In[6]:


if 0 < x and x < 10:
    print('x is a positive single-digit number.')


# ## Glossary of control flow terms
# 
# * `if`
# * `elif`
# * `else`
# * `and`
# * `or`
# * `not`
# * `in`
# * `==`
# * `>`
# * `>=`
# * `<`
# * `<=`
# * `!=`

# ## Exercises: control flow
# 
# **Exercise 3.1**
# 
# Here are two variables containing sequences:
# 
# ```python
# a = 'GCTAGGCAGGTGCAGGGGTAG'
# b = 'GGCAGATAGGACAGTGAGGGACATAGACCATAGACGANCATGACTTAG'
# ```
# 
# Write a block of statements that provides an answer to the question whether:
# 
# * the sequence of `a` is the same as the sequence of `b`
# * `a` is longer than `b`, shorter than `b`, or the same length as `b`
# * which of the sequences (if any) contains an `'N'`
# 
# **Exercise 3.2**
# 
# Take the following DNA sequence.
# 
# ```python
# dna = "TTGCATGTCAATCGATCGGATTGGTTGATTTATCCCGA"
# ```
# 
# Write code that will print `*` if there is a stop codon in this sequence (TAA, TAG or TGA).
# 
# **Exercise 3.3**
# 
# Read the description and methods of the UCSC CpG island track: [https://genome.ucsc.edu/cgi-bin/hgTrackUi?g=cpgIslandSuper](https://genome.ucsc.edu/cgi-bin/hgTrackUi?g=cpgIslandSuper).
# 
# Write the code that will test if a sequence is a CpG island. You can test your code with the following sequences (only the first is a CpG island):
# 
# ```python
# #chr15:74022901-74023101
# seq1 = ("AAGTGCGACATCAGCGCAGAGATCCAGCAGCGACAGGAGGAG"
#         "CTGGACGCCATGACGCAGGCGCTGCAGGAGCAGGATAGTGCC"
#         "TTTGGCGCGGTTCACGCGCAGATGCACGCGGCCGTCGGCCAG"
#         "CTGGGCCGCGCGCGTGCCGAGACCGAGGAGCTGATCCGCGAG"
#         "CGCGTGCGCCAGGTGGTAGCTCACGTGCGGGCGT")
# 
# #chr15:74022838-74023029
# seq2 = ("CGAGGATGTTCCAAGCCGCTGTGCTGCTCGTGCGCGCTCCTT"
#         "GACAGCAGCCACAGTGAGCTCAAGTGCGACATCAGCGCAGAG"
#         "ATCCAGCAGCGACAGGAGGAGCTGGACGCCATGACGCAGGCG"
#         "CTGCAGGAGCAGGATAGTGCCTTTGGCGCGGTTCACGCGCAG"
#         "ATGCACGCGGCCGTCGGCCAGCTG")
# 
# #chr15:74022489-74022698 
# seq3 = ("AGATGTGTGGAAGGGTGCACCCCACGATGCTCACCTGGTGCT"
#         "TCCTCGGTGGGGAAGGGAAATTCAGAAGTGGTGGAAAGAGAT"
#         "GATTGTCGTTTCGTATATCTTTGTATTGTTTCCCGGATGTTG"
#         "AAATTGTTACTGTAGTAACTTTTTATACTCATGTGTTATTGG"
#         "TAGTTTGGATACTATCACCATAACCACAAACACTGAATTAGG")
# ```

# In[ ]:




