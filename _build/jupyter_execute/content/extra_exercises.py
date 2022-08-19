#!/usr/bin/env python
# coding: utf-8

# # Assembling the pieces
# 
# In this chapter, no new Python topics will be introduced. You will practice by writing functions that combine the different topics that we have covered.
# 
# ## Exercises

# **Exercise 7.1: Translation**
# 
# Write a function `mrna2protein` that converts an mRNA sequence (using the A,C,G,T alphabet) into
# a protein sequence.
# You can use the codon table that was used in **exercise 6.9**.

# In[1]:


def mrna2protein(seq):
    # Adapt this function with your own code
    
    return prot


# **Exercise 7.2: Open reading frames**
#  
# Write a function `longest_orfs` that will take a DNA sequence as input and returns the protein sequence encoded by
# the longest ORF for all three frames. The return value should be a dictionary, with the frame number as the key and the
# protein sequence as the value. This means that the dictionary will have three `key:value` pairs. The three keys are `1`,
#  `2` and `3` and the corresponding values are the longest ORF for frame 1, the longest ORF for frame 2 and the longest ORF for frame 3.
# 
# The stop codon (`*` in the amino acid table) should not be included in the translation of the ORF. For this exercise an open reading frame does not need to start with an ATG, it can start with any codon, except a stop codon.
# For example, take the sequence `"actgcgtagagagctggagagattaggc"`. The translation of the full sequence for frame 1 would look like this:
#  
# ```
# TA*RAGEIR
# ```
# 
# In this example, the longest ORF is `RAGEIR`.
# 
# You can re-use code that you have written for **exercise 4.8** and **exercise 7.1**.
# 

# In[2]:


def longest_orfs(seq):
    # Adapt this function with your own code
    return orfs


# **Exercise 7.3: Hamming distance**
# 
# Write a function called `hamming` that takes two strings `s` and `t` of equal length as arguments and computes the number of differences between them.
# The function should return the number of symbols that differ in `s` and `t`.
# 

# In[3]:


def hamming(s, t):
    # adapt this function with your own code
    return 0

print(hamming("ACTG", "ACTG"))
print(hamming("ACTG", "GTCA"))
print(hamming("AACC", "AATT") + hamming("CTGA", "TCGA"))


# If your function is defined correctly, the code above should exactly match the following output when run:
# 
#     0
#     4
#     4
# 
# **Exercise 7.4 Find exact motif matches**
# 
# Given two strings `s` and `t`, `t` is a substring of `s` if `t`
# is contained as a contiguous collection of symbols in `s` (as a result,
# `t` must be no longer than `s`).
# Write a function called `find_match` that takes two arguments, `s` and `t`,
# and returns a `list` of all positions of the substring `t` in `s`.

# In[4]:


# define your function here


# When you have finished the function run the code below:
# 
# ```python
# # Don't change anything here, but update the function definition above!
# print(find_match("GATATATGCATATACTT", "ATAT"))
# print(find_match("AUGCUUCAGAAAGGUCUUACG", "U"))
# ```

# Instead of giving an error, the output above should *exactly* match the following:
# 
#     [2, 4, 10] 
#     [2, 5, 6, 15, 17, 18] 
# 

# **Exercise 7.5: Motif conversion**
# 
# Write a function that converts a consensus sequence into a positional weight matrix.
# The consensus sequence can be composed of symbols from the [IUPAC DNA code](http://www.bioinformatics.org/sms2/iupac.html).
# The function should ignore any non-IUPAC character. The positional weight matrix should be a two-dimensional list.
# Every element in the first list is a list containing the relative frequencies of A, C, G and T, in that specific order, that together sum up to `1.0`.
# The function should work, regardless of the input being upper-case, lower-case or a mix.

# **Exercise 7.6: Analysis of a regulatory network** 
# 
# For this question use the regulatory network represented in the following dictionary:
# 
# ```python
# hsc_network = {
#     "Scl" : ["Scl","Gata1","Gata2","Hhex","Zfpm1","Fli1","Erg","Smad6","Runx1","Eto2"],
#     "Pu.1" : ["Pu.1","Runx1","Gata1"],
#     "Runx1" : ["Runx1","Pu.1","Erg"],
#     "Smad6" : ["Runx1"],
#     "Eto2" : ["Erg"],
#     "Gata1" : ["Gata1","Scl","Pu.1","Gata2"],
#     "Fli1" : ["Fli1","Runx1","Pu.1","Scl","Gata2","Hhex","Erg","Smad6"],
#     "Erg" : ["Smad6","Runx1","Erg","Hhex","Gata2","Fli1"],
#     "Zfpm1" : ["Gata2"],
#     "Gata2" : ["Zfpm1","Runx1","Smad6","Eto2","Scl","Gata2","Hhex","Fli1","Erg"],
#     "Hhex" : ["Gata2"]
# }
# ```
# 
# Each key is a transcription factor and each value is a list of target genes.
# 
# Write a function `common_targets` that accepts three arguments: a TF-Target dictionary, and two TF
# names. The function should return a `list` with all the targets that are shared between the two TFs. The
# target `list` should be alphabetically ordered. When there are no common targets the function should return
# an empty `list`.
# With the network above, the following code:
# 
# ```python
# print(common_targets(hsc_network, "Scl", "Gata2"))
# print(common_targets(hsc_network, "Smad6", "Eto2"))
# print(common_targets(hsc_network, "Zfpm1", "Hhex"))
# ```
#                      
# Should result in:
# 
# ```python
# ['Erg', 'Eto2', 'Fli1', 'Gata2', 'Hhex', 'Runx1', 'Scl', 'Smad6', 'Zfpm1']
# []
# ['Gata2']
# ```

# In[ ]:




