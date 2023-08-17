#!/usr/bin/env python
# coding: utf-8

# # Files
# 
# ## Introduction to files
# 
# Thus far we have used Python without reading input from files and writing output to files. We have created objects like lists and dictionaries, but nothing has been saved persistently, meaning that if we close Python, everything is gone. Usually you want to open a file, read its contents (line by line), analyze it, and write it to another file. To work with files we need the Python `file` object. `file` objects serve as a *link to a file* residing on a disk or cloud.
# 
# To open a file, write some contents to it and close it:

# In[1]:


myfile = open('testfile.txt', 'w')
myfile.write('some text\n')
myfile.close()


# Note the following:
# 
# *  `myfile` is the name of the Python `file` *object*
# *  `'testfile.txt'` is the name of the *file* written to the disk or the cloud
#     * extension is not important, but suggests that it contains text
# *  The `'w'` argument to the `open()` function opens the file for *writing*
# *  If the file `'testfile.txt'` already exists, you will overwrite its contents
# *  If not, the file `'testfile.txt'` will be created 
# *  You can also use `'a'` instead, which would *append* any output to the existing file called `'testfile.txt'`
# *  If you use `'r'` instead, you only open the file for only *reading* (it has to exist of course)
# *  `write()` is a method belonging to the `file` object 
# *  `write()` does not add a newline character to the end of a line, that is why we add `\n` to our text
# *  `close()` is a method belonging to the `file` object
# 
# 
# 

# ```{note}
# The file `'testfile.txt'` is written to your Google Colab `/content` folder, and will be visible in the file-explorer pane once you refresh it. However, your Google Colab `/content` folder is temporary and will be cleared after a few hours. 
# ```
# 
# To save the file permanently, you can write it to Google Drive:
# 
# ```python
# from google.colab import drive
# drive.mount('/content/gdrive')
# 
# # choose the Google account that you want to use, and allow access
# 
# myfile = open('/content/gdrive/MyDrive/testfile_gdrive.txt', 'w')
# myfile.write('this file is saved in Google Drive \n')
# myfile.close()
# ```

# To work with an existing file, we could open it and work on the complete contents in the file. However, sometimes the files used for our analyses are very large. If the file contains lines of text, we may rather open the file, process its contents *line-by-line*, and write output to another file. 
# 
# To open a file and read its contents line-by-line we first open the file using `open()`. To step through the file line-by-line we use a `for` or `while` loop to 'iterate' over the resulting `file` object. *Each iteration returns a line of the file, from top to bottom*.
# 
# The `for` or `while` loop automatically ends as soon as there are no lines anymore (=after the last line).
# 
# At the end of the code that you execute for each line, you should close the file. 

# In[2]:


infile = open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r')
for line in infile:
    print(line)
infile.close()


# In[3]:


infile = open('../data/example.bed', 'r')
for line in infile:
    print(line)
infile.close()


# The file `/content/gdrive/MyDrive/CFB_files/example.bed` is an example BED file. BED files are used to store genomic coordinates along with additional information. BED files are for instance used to store genomic coordinates of ChIP-seq peaks. The first three fields (columns) contain the chromosome, start, and end of the features, respectively. The file `/content/gdrive/MyDrive/CFB_files/example.bed` also contains 'header' lines that are used when the file is displayed in the UCSC genome browser. This is not always the case for BED files.

# While the code above functions just fine, it is nowadays more common in Python to open files with the `with` statement.

# In[13]:


with open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r') as infile:
    for line in infile:
        print(line)


# You see that the code is very similar. However, you don't have to explicitly close the file. As soon as the code exits the `with` block, the file is closed automatically.

# ```{note}
# The `with` statement is the preferred way to work with files.
# ```

# In the next few examples we will see some analysis of this file in action. Each example adds some steps and builds from the previous example. 
# 
# Example 1:
# 
# * open the `/content/gdrive/MyDrive/CFB_files/example.bed` file
# * read the file line-by-line
# * ignore header lines starting with 'browser' or 'track'
# * split each line into a list based on the `<tab>` character
# * print each line
# * print the values

# In[14]:


with open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r') as infile:
    for line in infile:        # use a variable called 'line' for each line
        line = line.strip()    # take away the '\\n' character at the end of each line
        # only proceed with lines lacking 'browser' or 'track' at the beginning
        if not line.startswith('browser') and not line.startswith('track'):
            # split the line (`string`) into a `list`, with the '\\t' as a delimiter
            vals = line.split('\t')
            print(vals)


# Note how we used `startswith()` to check if a string starts with 'browser' or 'track'
# 
# 
# Example 2:
# 
# * assign the first three elements of this list to the variables `chrom`, `start`, and `end`

# In[15]:


with open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line.startswith('browser') and not line.startswith('track'):
            vals = line.split('\t')
            chrom, start, end = vals[0:3]  
            print(chrom, start, end)


# 
# Example 3:
# 
# * convert the `start` and `end` variables to an integer `int` (they are strings at first)
# * calculate the width (size in bases) of each feature

# In[9]:


with open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r') as infile:
    for line in infile:              
        line = line.strip()          
        if not line.startswith('browser') and not line.startswith('track'):
            line = line.split('\t')  
            chrom, start, end = line[0:3]      
            start = int(start)    # convert start to `int`
            end = int(end)        # convert end to `int`
            width = end - start
            print(width)


# Example 4:
# 
# * calculate how many features with strand '+' and strand '-' are present
# 

# In[10]:


plus = 0
minus = 0
with open('/content/gdrive/MyDrive/CFB_files/example.bed', 'r') as infile:
    for line in infile:
        line = line.strip()
        if not line.startswith('browser') and not line.startswith('track'):
            vals = line.split('\t')
            strand = vals[5]
            if strand == '+':
                plus = plus + 1
            elif strand == '-':
                minus = minus + 1

print(plus, minus)


# Thus far we have used the `print()` statement to print output to the screen. But if you want to be more explicit in the formatting of the output, you should use `format()`, which creates a `string` that can either be printed or written to a file. The standard way of using `format()` is like this: `'some text {} more text {}'.format(var1, var2)`. See the following example in which `format()` is used:
# 

# In[3]:


cell_lines = ['HCT116', 'HeLa', 'HEK293']
for i in range(3):
    args = 'Cell line {} is {}'.format(i + 1, cell_lines[i])
    print(args)


# Note that the `print()` statement by default adds a newline character `"\n"`. If you write to a file you need to add the newline character `"\n"` to the string:

# In[11]:


with open('cell_lines.txt', 'w') as outfile:
    cell_lines = ['HCT116', 'HeLa', 'HEK293']
    for i in range(3):
        args = 'Cell line {} is\t{}\n'.format(i + 1, cell_lines[i])
        outfile.write(args)


# Note how we also used `"\t"` here. This is the character that specifies a `<tab>`.
# 

# ## Glossary of file terms and functions
# 
# * `open()`
# * `with`
# * `for`
# * `while`
# * `write()`
# * `startswith()`
# * `format()`

# ## Exercises: files
# 
# **Exercise 8.1: FASTA files**
# 
# The FASTA format is a widely used text format to represent nucleotide or peptide sequences. If you do not know what a FASTA file is, read the [NCBI FASTA specification](https://blast.ncbi.nlm.nih.gov/doc/blast-topics/#fasta) carefully.
# 
# In this exercise, write a function `read_fasta` that reads a multiple sequence FASTA file. 
# The function should take the file name as an argument, and return a dictionary with the sequence identifier as key and the actual sequence as value. Note that the `>` symbol is not part of the sequence identifier.
# You can start by using a file called `testfile.fasta` (present in `/content/gdrive/MyDrive/CFB_files`), which is a small FASTA file. 
# 
# <details>
# <summary> If you are struggling with this exercise, click on the triangle to view tips. </summary>
# 
# First, mount Google Drive. Then, find this file in the Google Drive folder:
#     `/content/gdrive/MyDrive/CFB_files/testfile.fasta`
# 1.	This file is a FASTA file. What do you know about FASTA files? 
# 2.  Double click on the file to open it, to check out what it looks like. You can do this directly in Google Colab, like this: 
#     ![](img/gdrive_open_testfile_fasta.png)
# 3.	Describe the contents of the file in your own words. There are two types of lines in this file: some are "sequence identifiers" and some are "sequences". How can you tell which is which?
# 4.	Now, in your Notebook, open the file up in python and read this file line by line. (You learned how to do this in the "Introduction to files" section in this chapter.) Save each line into one single (large) `list`. Don’t forget to close the file if you need to - this depends on how you opened the file.
# 5.	Now you have a `list`. There are two types of items in the list: some are "sequence identifiers" and some are "sequences". Can you find a pattern in how these two types of items are organized?
# 6.	Now write a dictionary with every "sequence identifier" as the key, and the "sequence" immediately after it as the value. To do this, first create an empty `dictionary`, then add `key`-`value` pairs to the dictionary one at a time. Use loops and conditionals.
# 
# You have now written most of the code necessary for this exercise. Read the exercise again. What does the exercise ask for? What do you have to do to turn your code from above into the "real" answer?
# 
# Once you have written your function, you can use these files to test it out:
# * `/content/gdrive/MyDrive/CFB_files/STAT3.fa`
# * `/content/gdrive/MyDrive/CFB_files/c-Myc.fa`
# 
# (Note that both the `.fa` file-extension and the `.fasta` file-extension denote FASTA files.)
# 
# </details>
# 
# <br/>
# 
# 

# **Exercise 8.2: convert gene annotation file**
#     
# The file `/content/gdrive/MyDrive/CFB_files/genes.txt` contains gene annotation. Each line represents one gene. The file is
# tab-separated and contains the following columns:
# 
# ```
# 1 - chromosome
# 2 - gene start
# 3 - gene end
# 4 - strand
# 5 - gene name
# 6 - number of exons
# 7 - a comma-separated list of exon sizes
# 8 - a comma-separated list of exon starts, relative to the gene start
# ```
# 
# Write a function called `gene2exons` that reads the gene annotation from this file and converts it to a file with exon information. The function should accept two arguments, the `input_file` and the `output_file`. The output should be tab-separated and will contain 5 columns:
# 
# ```   
# 1 - chromosome
# 2 - exon start
# 3 - exon end
# 4 - exon name: gene name followed by a . and the exon number
# 5 - strand
# ```
# 
# For instance, for the gene SALL4 the output should look like this:
# 
# ```
# chr20 51782330 51784684 SALL4.1 -
# chr20 51788860 51789141 SALL4.2 -
# chr20 51790021 51792352 SALL4.3 -
# chr20 51802278 51802520 SALL4.4 -
# ```
# 
# The gene SALL4 has four exons, which are numbered from 1 to 4. Exon numbers are not dependent on the
# strand, they are numbered from low start position to high start position.

# **Exercise 8.3**
# 
# In this exercise you are going to analyze data from ChIP-seq of several transcription factors in mouse embryonic stem cells ([Chen et al. 2008, 13;133(6):1106-17, PMID 18555785](https://pubmed.ncbi.nlm.nih.gov/18555785/)). Please have a look at Figure 1 and 2 of this paper. Figure 1 shows the ChIP-seq profiles for the transcription factors.
# 
# The ChIP-seq peaks that you see represent *in vivo* binding sites of these transcription factors. In Figure 2 the authors have analyzed the DNA sequence underneath these peaks, and identified specific DNA sequences (**motifs**) for each transcription factor. 
# 
# You are going to analyze these sequences as well, to see which motifs you can identify. You will count **k-mers** (short sequences, e.g. 8 bases in length) in the sequences underneath the ChIP-seq peaks of a specific transcription factor, and analyze which k-mers are overrepresented.
# 
# DNA (or amino acid) sequence files are usually in [FASTA format](https://en.wikipedia.org/wiki/FASTA_format). Before you start off using the FASTA files from the study mentioned above, work on a file called `testfile.fasta` (present in `/content/gdrive/MyDrive/CFB_files`), which is a small FASTA file. This allows you to make and test your code quicker.
# 
# 1. Provide the Python code that allows you to read the FASTA file while ignoring the description lines containing `>`. For now it is OK to print the output. 
# 
# 2. Extend your code with the following: For each sequence, extract all possible k-mers of length 4. Skip sequences that are shorter than 4 bases. Print the output. Make sure your code allows you to easily run the same analysis with different k-mer lengths.
# 
# 3. Extend your code with the following: Count the number of occurrences for each k-mer that is encountered (in all sequences together).
# 
# 4. Extend your code with the following: Write the top 10 most abundant k-mer sequences to an output file, along with the number of times they occur.
# 
# 5. Now that you have assembled your code (you can remove the printing statements you used for testing) adapt your code to count kmers of **length 8**. Run your code on 2 files present in the `/content/gdrive/MyDrive/CFB_files` directory:
# 
#   * `GSM288346_ES_Oct4_mm9.peaks.fasta`
#   * `GSM288356_ES_c-Myc_mm9.peaks.fasta`
#   * `GSM288353_ES_Stat3_mm9.peaks.fasta`
#   * `GSM288354_ES_Klf4_mm9.peaks.fasta`
# 
# For the top most occurring 8-mers that you obtained for each file, do these resemble the motifs for the corresponding transcription factors as displayed in Figure 2 of the paper?
# 
# 6. Write a function called `top_kmers()`. The function should have three arguments: `fname`, `k`, `n_top`. The `fname` represents the FASTA filename, `k` the length of the k-mer and `n_top` the number of most abundant k-mers to return. The function should not print the k-mers, but return them as a list. The `k` and `n_top` arguments should be *optional*, with default values of 8 and 10, respectively.
