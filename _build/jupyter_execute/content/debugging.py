#!/usr/bin/env python
# coding: utf-8

# # Debugging
# 
# ## Exercises: debugging
# 
# **Exercise 10.1**
# 
# The purpose of the following code is to count how often each TF in the network is a target of a TF in the network (it also counts if a TF regulates itself).
# In other words, how many TFs in the network bind in the promoter of a given TF.
# 
# * The below code is provided in the script `exercise4_with_errors.py`. 
# * Use the terminal and command line to copy the file to a new file named `my_exercise4.py`.
# * Edit the new file by clicking on it in the Jupyter browser.
# * Every time you change the file, save it.
# * Execute the Python script from the command line with `python my_exercise4.py`.
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

# ```{hint}
# There are multiple *bugs* in the code below. Some are obvious mistakes (a typo). 
# However, some are mistakes that do not produce runtime errors that produce an incorrect result.
# ```
# 

# In[2]:


# define HSC network from Bonzanni et al, Bioinformatics 2013
hsc_network = {                                # each key is a source TF, the value for each key is a list of target TFs
        "Scl" : ["Scl","Gata1","Gata2","Hhex","Zfpm1","Fli1","Erg","Smad6","Runx1","Eto2"],
        "Pu.1" : ["Pu.1","Runx1","Gata1"],
        "Runx1" : ["Runx1","Pu.1","Erg"],
        "Smad6" : ["Runx1"],
        "Eto2" : ["Erg"],
        "Gata1" : ["Gata1","Scl","Pu.1","Gata2"],
        "Fli1" : ["Fli1","Runx1","Pu.1","Scl","Gata2","Hhex","Erg","Smad6"],
        "Erg" : ["Smad6","Runx1","Erg","Hhex","Gata2","Fli1"],
        "Zfpm1" : ["Gata2"],
        "Gata2" : ["Zfpm1","Runx1","Smad6","Eto2","Scl","Gata2","Hhex","Fli1","Erg"],
        "Hhex" : ["Gata2"]
        }

target_frequencies = [0,0,0,0,0,0,0,0]         # How often is each TF a target of another TF?
list_of_tfs = []                               # list of transcription factors in the network

tf_to_index = {}                               # dictionary linking TF name to numerical index in list

index = 0                                      # initialize index to zero
for tf in hsc_network:
    list_of_tfs.append(tf)                     # append tf to the list of transcription factors in the network
    index = index + 1  # update index

    tf_to_index[tf] = index                    # associate the transcription factor tf with the index


for source_tf in hsc_network:                  # iterate over TFs in the network
    list_of_target_tfs = hsc_network[source_tf]
    for target_tf in list_of_target_tfs:       # iterate over all TFs that are targeted by source_tf
        index_in_list = tf_to_index[target_tf] # retrieve list index associated with this TF
        target_frequencies[index_in_list] = target_frequency[index_in_list] + 1

for index in range(len(list_of_tfs)):
    tf = list_of_tfs[index]
    target_frequency_tf = target_frequencies[ index ]
    print("Transcription factor",tf,"is",target_frequency_tf,"times a target of another TF")

print("Finished analysis of HSC network")


# **Exercise 10.2**
# 
# The following code (provided in the file `exercise5.py`) 
# tests whether a particular TF of interest directly regulates itself (in other words, if a TF binds in its own promoter).
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
# 2. Run the code as a script from the command line in a terminal.
#  Does the code run without error?
# 3. Does the code provide the correct output for the TF named 'Scl'?
# 4. Does the code provide the correct output for all TFs? 
# If not, how would you adapt the code (extend or change it) so that it does produce the desired output?
# 

# In[3]:


# Does a TF regulate itself?

# each key is a source TF, the value for each key is a list of target TFs
hsc_network = {                                
        "Scl" : ["Scl","Gata1","Gata2","Hhex","Zfpm1","Fli1","Erg","Smad6","Runx1","Eto2"],
        "Pu.1" : ["Pu.1","Runx1","Gata1"],
        "Runx1" : ["Runx1","Pu.1","Erg"],
        "Smad6" : ["Runx1"],
        "Eto2" : ["Erg"],
        "Gata1" : ["Gata1","Scl","Pu.1","Gata2"],
        "Fli1" : ["Fli1","Runx1","Pu.1","Scl","Gata2","Hhex","Erg","Smad6"],
        "Erg" : ["Smad6","Runx1","Erg","Hhex","Gata2","Fli1"],
        "Zfpm1" : ["Gata2"],
        "Gata2" : ["Zfpm1","Runx1","Smad6","Eto2","Scl","Gata2","Hhex","Fli1","Erg"],
        "Hhex" : ["Gata2"]
        }

my_tf_of_interest = 'Scl'

for target_tf in hsc_network[my_tf_of_interest]:
    if target_tf == my_tf_of_interest:
        my_tf_regulates_itself = True

if my_tf_regulates_itself:
    print("Transcription factor",my_tf_of_interest,"regulates itself")
else:
    print("Transcription factor",my_tf_of_interest,"does not regulate itself")


# **Exercise 10.3**
# 
# This exercise focuses on problems that may arise when an input file does not have the formatting you expect, contains errors or otherwise unexpected events.
# 
# For small networks it is feasible to type your network directly as a dictionary, like in the example above. 
# In other realistic scenarios, the network file is produced by another analysis (either your own Python script or another program), and you would like
# to analyze the network produced by that program.
# 
# The purpose of the below code is to determine which TFs are provided in a flat text file, and count *how many* target genes each TF has. 
# To keep things managable, the text file contains only a small network.
# 
# The setting is as follows:
# 
# * We have a flat text input file containing the network links in the following format:
# 
#     source_tf_1 target_1 target_2 target_3
#     source_tf_2 target_4 target_5
# 
# * We want to parse the input file and count for each source_tf that occurs how many targets it has.
# * To test the correctness of our code, we provide you with an input file that has several issues that cause the program 
# to misbehave.
# 
# The following code is contained in the script `exercise6.py`. 
# It reads a network from the file `network_exercise_6.txt`.  
# The code contained in it is as follows:

# In[5]:


target_tfs_dict = {} # will contain a list of the target genes for each source gene

input_file = open("/content/gdrive/MyDrive/CFB_files/network_exercise_6.txt",'r') # change path/filename if you want to run it on a different file

for line in input_file:
    entries = line.strip().split()
    source_tf = entries[0]   # source TF is always the first string in a line
    targets = entries[1:] # the strings after the first one are the target genes
    target_tfs_dict[source_tf] = targets

input_file.close()

for tf in sorted(target_tfs_dict):
    print("Source TF:\t",tf,"\tNumber of targets:\t",len(target_tfs_dict[tf]))


# Run the script from the command line in a terminal. You can view the network file by clicking on it in the Jupyter file browser. 
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
# The script `exercise6.py` makes three assumptions about the input file that are not valid (the input file violates the assumption).
# 
# Describe at least three assumptions that this script makes about the input file and provide a script that produces the desired output.
# 
# For example, describe the assumptions as specifically as in the following examples (this is just an example, not relevant to this script):
# 
# * The script assumes that each line has precisely 20 characters
# * The script assumes that each line starts with a capital letter
# 
# ```{note}
# You have the change the Python script; you are **NOT** allowed to change the input file!
# ```
# 
# **Hints:**
# 
# 1. Use `if` statements to check whether a specific assumption that you require for correct execution is satisfied.
# For instance, you can use an `if` statement to check the length of a list, or whether a key is present in the dictionary.
# 2. Add `print()` statements to understand what each line is doing and what the value is of a variable.
# 3. You are allowed to change the input file to understand where the problem is, but you have to provide code that produces the correct output for the original input file.
# 
# 
# [comment1]: # (Assumes at least 1 target on each line)
# [comment2]: # (Assumes no duplicates / assumes all targets of a TF are on the same line)
# [comment3]: # (Assumes the separator is always a space)
