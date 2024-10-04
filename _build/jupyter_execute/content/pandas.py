#!/usr/bin/env python
# coding: utf-8

# # Introduction to pandas DataFrames
# 
# In this tutorial you are going to use the module `pandas`.
# We will focus on DataFrames, a convenient object type used in pandas.
# 
# ```{note}
# This tutorial has no exercises, but serves as an introduction to pandas.
# It will illustrate what you can do with pandas DataFrames. 
# ```
# 
# If you want more information on pandas, a (quick) tutorial is found here:
# 
# [https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
# 
# ## Importing the pandas module
# 
# We start by importing the `pandas` module, for which we use the following command:

# In[1]:


import pandas as pd


# Note that we imported the `pandas` module and renamed it to `pd`. This allows us to use all `pandas` functionality using `pd` (instead of `pandas`). This is very common: it saves typing since `pd` is shorter than `pandas`.

# ## Creating a pandas DataFrame from lists
# 
# Here we will create a pandas DataFrame containing the following columns:

# In[2]:


chrom = ['chr6', 'chr11', 'chr3', 'chr2', 'chr17', 'chr17']
start = [143889976, 77774406, 14988512, 203102822, 7590368, 26903451]
end = [143890976, 77775406, 14989512, 203103822, 7591368, 26904451]
refseq =['NR_027113', 'NM_003251', 'NR_046253', 'NM_003352', 'NM_001126112', 'NM_005165']


# In this case we create an empty DataFrame first, and we fill it up with the individual columns.
# 

# In[3]:


df_peaks = pd.DataFrame()

df_peaks['chrom'] = chrom
df_peaks['start'] = start
df_peaks['end'] = end
df_peaks['nearest_gene'] = refseq


# You can check what your DataFrame looks like using  `print()`, or simply type `df_peaks`. The latter only works in a Jupyter notebook, but the advantage is that you get a nicely formatted table!

# In[4]:


print(df_peaks)


# In[5]:


df_peaks


# We make a second DataFrame, which corresponds to a second experiment ('exp2')
# 

# In[6]:


chr_exp2 = ["chr6_dbb_hap3", "chr7", "chr9", "chrX", "chrX", "chrX"]
start_exp2 = [4324541, 98029927, 90497271, 71496641, 73506544, 152162171]
end_exp2 = [4325541, 98030927, 90498271, 71497641, 73507544, 152163171]
refseq_exp2 = ["NM_002121", "NM_018842", "NM_178828", "NM_001007", "NR_030258", "NM_001184924"]

df_peaks_exp2 = pd.DataFrame()
df_peaks_exp2['chrom'] = chr_exp2
df_peaks_exp2['start'] = start_exp2
df_peaks_exp2['end'] = end_exp2
df_peaks_exp2['nearest_gene'] = refseq_exp2


# Look at both DataFrames. The `head()` function shows the first five rows of a DataFrame.
# 
# They have the same column layout (`chrom`, `start`, `end`, `refseq`).

# In[7]:


df_peaks.head()


# In[8]:


df_peaks_exp2.head()


# They both represent peaks of a ChIP-seq experiment.
# 
# For both DataFrames we can add an additional column indicating from which experiment the data comes ('exp1' or 'exp2')
# 

# In[9]:


df_peaks['exp'] = 'exp1'
df_peaks_exp2['exp'] = 'exp2'


# Take a look at the two DataFrames, and note how we did this:
# 
# * We used `[ ]` to define a new colum, with the column name between `[ ]`
# * We used only one string (`'exp1'` or `'exp2'`), but this was automatically expanded to the whole column
# 
# 
# ## Creating a pandas DataFrame using a `dictionary`
# 
# We can also create a pandas DataFrame from a dictionary. The dictionary should contain *column names as keys* and *lists as values* for the columns. To show this in action, we will use the three following lists:
# 

# In[10]:


refseq = ["NM_001007", "NM_001098638", "NM_001110221", "NM_001126112", "NM_001142599", 
          "NM_001164283", "NM_001164386", "NM_001184924", "NM_001290043","NM_002121",
          "NM_002441", "NM_003251", "NM_003352", "NM_004263", "NM_005165", "NM_006017",
          "NM_007145", "NM_016522", "NM_018842", "NM_024097", "NM_147181", "NM_173856",
          "NM_178828"]

ensembl = ["ENSG00000198034", "ENSG00000166439", "ENSG00000121742", "ENSG00000141510",
           "ENSG00000072682", "ENSG00000056972", "ENSG00000158987", "ENSG00000198883",
           "ENSG00000225967", "ENSG00000237710", "ENSG00000235569", "ENSG00000151365",
           "ENSG00000116030", "ENSG00000135622", "ENSG00000109107", "ENSG00000007062",
           "ENSG00000167635", "ENSG00000182667", "ENSG00000006453", "ENSG00000164008",
           "ENSG00000185774", "ENSG00000196131", "ENSG00000177992"]

genename = ["RPS4X", "RNF169", "GJB6", "TP53", "P4HA2", "TRAF3IP2", "RAPGEF6", "PNMA5", 
            "TAP2", "HLA-DPB1", "MSH5", "THRSP", "SUMO1", "SEMA4F", "ALDOC", "PROM1",
            "ZNF146", "NTM", "BAIAP2L1", "C1orf50", "KCNIP4", "VN1R2", "SPATA31E1"]


# First, we use these lists to create a dictionary
# 

# In[11]:


dict_genes = {
    'refseq': refseq,
    'ensembl': ensembl,
    'genename': genename
}


# Now that we have the dictionary, we can create the DataFrame.
# 

# In[12]:


df_genes = pd.DataFrame(dict_genes)


# Look at the resulting DataFrame called `df_genes`. This DataFrame will help us to map RefSeq to ENSEMBL gene identifiers.

# The first three rows.

# In[13]:


df_genes.head(3)


# The last three rows.

# In[14]:


df_genes.tail(3)


# Or three random rows.

# In[15]:


df_genes.sample(3)


# Next, we create another DataFrame with gene expression values
# 
# Here, we will use the dictionary method to create a `DataFrame` without explicitly creating the dictionary.

# In[16]:


ensembl_1 = ["ENSG00000237710", "ENSG00000182667", "ENSG00000121742", "ENSG00000158987", 
             "ENSG00000196131", "ENSG00000151365", "ENSG00000056972", "ENSG00000235569", 
             "ENSG00000006453", "ENSG00000198883", "ENSG00000225967", "ENSG00000166439", 
             "ENSG00000135622", "ENSG00000007062", "ENSG00000109107", "ENSG00000167635", 
             "ENSG00000164008", "ENSG00000141510", "ENSG00000177992"]

sample_1 = [None, 1.686, 0.063, 4.222, 0.021, 0.026, 8.169, None, 16.159, 0.08, None, 
            3.972, 0.844, 26.208, 18.218, 91.049, 3.828, 58.697, 0.024]

sample_2 = [None, 1.159, 0.011, 4.291, 0.004, 0.013, 0.306, None, 12.671, 0, None, 
            6.983, 5.352, 14.336, 5.333, 60.28, 5.137, 47.569, 0]

sample_3 = [None, 6.865, 0, 4.727, 0.039, 0.023, 10.459, None, 0.225, 0.011, None, 
            7.007, 3.402, 6.076, 18.445, 28.716, 4.128, 34.299, 0]

sample_4 = [None, 15.691, 2.16, 5.284, 0, 0.181, 1.428, None, 0.184, 0.395, None, 
            11.842, 4.186, 6.01, 131.013, 25.126, 9.933, 28.18, 0]


# In[17]:


# The next code could all be written on one line. However, to improve readability
# we write in this manner.
df_expr = pd.DataFrame(
    {
        'ensembl': ensembl_1, 
        'sample1': sample_1, 
        'sample2': sample_2, 
        'sample3': sample_3, 
        'sample4': sample_4
    }
)


# Look at the DataFrames using `print()` or, in Jupyter, by just typing the DataFrame name followed by `<Enter>`.
# 
# In the case where you would have very large DataFrames, you can always use `df.head()` to show the first rows, or `df.tail()` to show the last rows, where `df` is your DataFrame name.

# ## Merging pandas DataFrames
# 
# 
# ### Merging DataFrames on column values
# 
# We now have 3 types of data in our 3 DataFrames:
# 
# * ChIP-seq peaks (`df_peaks`)
# * A RefSeq to ENSEMBL gene identifier mapping (`df_genes`)
# * Expression values of genes in 4 samples, with ENSEMBL identifiers (`df_expr`)
# 
# This is a typical example for any (bioinformatical) analysis in which you want to incorporate different data types, often from different sources. You need to merge them if you want to do anything useful. Pandas DataFrames can be of big help here.
# 
# So let us try to merge these pieces of data.
# 
# ### Merging DataFrames: `concat`
# 
# Using the command `concat()` we can concatenate multiple DataFrames.
# Let us do this with the 2 ChIP-seq peaks DataFrames:

# In[18]:


df_all_peaks = pd.concat([df_peaks, df_peaks_exp2])
df_all_peaks


# Check out the result, and note how the `exp` column still allows us to distinguish the two experiments. 
# 
# You can use `concat()` to combine two DataFrames vertically (`axis=0`) or horizontally (`axis=1`).

# In[19]:


pd.concat([df_peaks, df_peaks_exp2], axis=0)


# In[20]:


pd.concat([df_peaks, df_peaks_exp2], axis=1)


# The [documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) contains more examples.
# 
# ### Merging DataFrames: `merge`
# 
# In the above case, we want to simply combine two DataFrames by concatenating, i.e. simply adding the rows of two DataFrames together. You can also join two DataFrames in other ways. The `df_peaks` DataFrame has a `nearest_gene` column. This is a RefSeq gene identifier that is also present in the `df_genes` DataFrame. If we would like to annotate the genes in `df_peaks`, we would only need the relevant columns for the genes that are in `df_peaks`. 

# In[21]:


df_genes_peaks = df_peaks.merge(df_genes, left_on="nearest_gene", right_on="refseq")
df_genes_peaks


# Check the resulting DataFrame. For every row in `df_peaks`, all the columns from `df_genes` have been added if the `refseq` identifier matches the identifier specified in `nearest_gene`.
# 
# Our DataFrame now has the ENSEMBL gene identifiers, so we can also merge the `df_expr`.

# In[22]:


df_genes_peaks_expr = df_genes_peaks.merge(df_expr, on='ensembl')


# Note that here the name of the columns that will be used for merging is the same in `df_genes_peaks` and `df_exp`, so we can use the `on='ensembl'` argument.

# For convenience, we will use a shorter name for our merged DataFrame

# In[23]:


df_all = df_genes_peaks_expr


# ## Tab completion and help
# 
# Now that we have merged our data, we can do several neat things.
# 
# Because `df_all` is a pandas DataFrame, it automatically inherits DataFrame methods.
# 
# You can get an idea if you type:
#     
#     df_all.
#     
# And then hit the left `<Tab>` key.
# 
# Notice that you get a lot of options....
# 
# Suppose you want to know how the `sort_values()` method for a DataFrame works. You can type:
# 
#     df_all.sort_values?
#     
# This HELP menu gives you information about the function. type `q` or `<ESC>` to leave the HELP.
# 
# ## Sorting a DataFrame
# 
# Let us try it out:

# In[24]:


df_all.sort_values(by='chrom')


# or

# In[25]:


df_all.sort_values(by='start')


# Note that these commands did not replace the original DataFrame `df_all`!
# 
# 
# ## Using `[ ]` to obtain DataFrame columns or rows
# 
# Using `[ ]` we can obtain specific parts of the DataFrame.
# 

# In[26]:


df_all['genename']


# In[27]:


## or, for multiple columns:
df_all[['genename', 'exp']]


# Using `iloc` we can do the same using indexes
# 
# One index by default points to **rows** of a DataFrame
# 
# To get the 2nd row, type:
# 

# In[28]:


df_all.iloc[0]


# Or, for multiple rows:

# In[29]:


df_all.iloc[1:3]


# This works very much like indexes of a `list`
# 
# If you use two indices, you can obtain specific rows *and* columns.
# 
# The first index is always *rows*, the second *columns*.
# 

# In[30]:


df_all.iloc[1:3, 4:11]


# ## Removing missing values or `NaN`s.
# 
# In many cases DataFrames contains `NaN`, missing values, and you often have to remove them.
# 
# 
# 
# 

# In[31]:


gene_info = pd.DataFrame({"full_name":["tumor protein p53", "aldolase, fructose-bisphosphate C"]},
                         index=["TP53", "ALDOC"])
df_all = df_all.join(gene_info, on="genename")
df_all


# We can obtain a `boolean` (`True`/`False`) for the column called `full_name` like this:

# In[32]:


df_all['full_name'].isnull()


# By using the `~` symbol we can invert this `boolean` column. The `~` acts as `not` for a pandas Series.

# In[33]:


~df_all['full_name'].isnull()


# We can use this strategy to remove all rows that have `NaN` in the column `full_name`.

# In[34]:


df_all[~df_all['full_name'].isnull()]


# 
# Make sure you understand how this worked!
# 
# 

# ## Basic calculations
# 
# There are a lot of methods that allows you to do basic calculation on DataFrames.
# 
# As an illustration we will calculate the pairwise correlations between the columns `sample1`, `sample2`, `sample3`, and `sample4`.
# 
# We take the appropriate columns first
# 

# In[35]:


df_1 = df_all[['sample1', 'sample2', 'sample3', 'sample4']]


# Now we can use the pandas `corr` method to calculate all pairwise correlations:

# In[36]:


df_1.corr()

