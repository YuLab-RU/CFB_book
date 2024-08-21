#!/usr/bin/env python
# coding: utf-8

# # Debugging
# 
# ## Exercises: debugging
# 
# **Exercise 9.1**
# 
# Find the notebook called `debugging_ex1.ipynb` in the Google Drive folder of the course. Save a copy of this notebook in your own Drive by going to File -> Save a copy in Drive.
# 
# The purpose of the code in this notebook is to count how often each TF in the network is a target of a TF in the network (it also counts if a TF regulates itself).
# In other words, how many TFs in the network bind in the promoter of a given TF.
# 
# There are multiple *bugs* in the code. Some are obvious mistakes (e.g. typos) that can lead to runtime errors. However, some are mistakes that do not produce runtime errors, but produce an incorrect output.
# The goal is to *debug* the code so that it runs without errors, and produces the correct output.
# 
# **Questions**
# 
# 1. What is the purpose of this code? (This should be obvious from the short description given above and the code itself)
# 2. What is the input and what is the expected output? 
# **Answer this question before running or changing the code, but make use of the network as defined in the dictionary `hsc_network`**.
# 3. Identify the source of the runtime errors, and fix the mistake into the code so that the script runs without error. 
# In that case, the last line of the output should be "Finished analysis of HSC network".
# 4. After you fixed the errors in the code, does the code produce the expected output? 
# 5. What is the output (list each TF and its target frequency)?
# 6. How would you solve this counting problem more elegantly? Hint: e.g. by using a single dictionary to replace the list `list_of_tfs` and dictionary `tf_to_index`.
# 
# Advice: make liberal use of `print()` statements to understand 
# 1. What each line in the code is trying to achieve
# 2. How to make the code function correctly, and make sure that it indeed functions correctly.

# **Exercise 9.2**
# 
# Find the notebook called `debugging_ex2.ipynb` in the Google Drive folder of the course. Save a copy of this notebook in your own Drive by going to File -> Save a copy in Drive.
# 
# The code in this notebook tests whether a particular TF of interest directly regulates itself (in other words, if a TF binds in its own promoter).
# The name of the TF of interest is assigned to the variable `my_tf_of_interest`.
# 
# The code should print 
# 
#     Transcription factor my_tf_of_interest regulates itself
# 
# or
# 
#     Transcription factor my_tf_of_interest does not regulate itself
# 
# to screen (with "my_tf_of_interest" replaced by the actual TF name), depending on whether there is a self-regulation relationship encoded in the
# `hsc_network` dictionary variable or not.
# 
# **Questions**
# 
# 1. This script contains a bug (otherwise it wouldn't be a question here). Can you identify the bug without running the code (try for at least 10 minutes)?
# 2. Run the code as it is given. Does the code provide the correct output for the TF named 'Scl'?
# 4. Change the variable "my_tf_of_interest" to different TFs in the dictionary `hsc_network`. Does the code provide the correct output for all TFs? 
# If not, how would you adapt the code (extend or change it) so that it does produce the desired output?
# 

# **Exercise 9.3**
# 
# This exercise focuses on problems that may arise when an input file does not have the formatting you expect, contains errors or otherwise unexpected events. 
# 
# In the Google Drive folder of the course, find the notebook called `debugging_ex3.ipynb`. Save a copy of this notebook in your own Drive by going to File -> Save a copy in Drive. 
# 
# In the Google Drive folder of the course, find a text file called `debugging_ex3_input.txt`. 
# Open this file (`debugging_ex3_input.txt`) to examine its contents. You can do this in any environment (Colab, Drive, or downloaded to your computer locally if you wish). This file contains a TF network in the following format:
# 
# ```
# source_tf_1 target_A target_B target_C
# source_tf_2 target_D target_E
# ```
# 
# Next, open the notebook `debugging_ex3.ipynb` and examine the code. The purpose of the code is to determine *which* `source_tf`s are given in the input file, and count *how many* `target_genes` each TF has. 
# However, the input file has several issues that causes our code to misbehave. 
# 
# Your goal in this exercise is to change the code so that it is able to recognize and handle issues in the input file. **You are not allowed to change the input file.**
# 

# 
# **Expected output**
# 
# If the script functions correctly, the desired output is:
# 
#     Source TF:	 Erg 	Number of targets:	 6
#     Source TF:	 Eto2 	Number of targets:	 1
#     Source TF:	 Fli1 	Number of targets:	 8
#     Source TF:	 Gata1 	Number of targets:	 4
#     Source TF:	 Gata2 	Number of targets:	 9
#     Source TF:	 Hhex 	Number of targets:	 1
#     Source TF:	 Pu.1 	Number of targets:	 3
#     Source TF:	 Runx1 	Number of targets:	 3
#     Source TF:	 Scl 	Number of targets:	 10
#     Source TF:	 Smad6 	Number of targets:	 1
#     Source TF:	 Zfpm1 	Number of targets:	 1
# 
# 
# **Question/assignment:**
# 
# Describe at least three assumptions that the code in `debugging_ex3.ipynb` makes about the input file. Describe the assumptions as specifically as in the following examples (this is just an example, not relevant to this script):
# 
# * The script assumes that each line has precisely 20 characters
# * The script assumes that each line starts with a capital letter
# 
# Then, provide a script that produces the desired output.
# 
# **Hints:**
# 
# 1. Use `if` statements to check whether a specific assumption that you require for correct execution is satisfied.
# For instance, you can use an `if` statement to check the length of a list, or whether a key is present in the dictionary.
# 1. Add `print()` statements to understand what each line is doing and what the value is of a variable.
# 2. You can create new input files to understand where the problem is, but you have to provide code that produces the correct output for the original input file.
# 
# 
# [comment1]: # (Assumes at least 1 target on each line)
# [comment2]: # (Assumes no duplicates / assumes all targets of a TF are on the same line)
# [comment3]: # (Assumes the separator is always a space)
