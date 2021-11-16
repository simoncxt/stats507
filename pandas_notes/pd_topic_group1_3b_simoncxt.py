#!/usr/bin/env python
# coding: utf-8

# <p>This is a short tutorial about neat pandas idioms. <a href="https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#idioms">idioms</a> .
# From Xiatian Chen email:simoncxt@umich.edu</p>
# <h1>Idioms</h1>
# <h2>If-then and splitting:</h2>
# <pre><code>    -Clear idioms allow the code to be more readable and efficient  
#     -Always need to construct data under specific conditions, here are some examples.
# </code></pre>
# <p><code>df = pd.DataFrame(
#     {"AAA": [4, 5, 6, 7], "BBB": [10, 20, 30, 40], "CCC": [100, 50, -30, -50]}
# )
# df.loc[df.AAA &gt;= 5, "BBB"] = -1</code>  </p>
# <pre><code>    -Can also apply if-then to multiple columns
# </code></pre>
# <p><code>df.loc[df.AAA &gt;= 5, ["BBB", "CCC"]] = 555</code>  </p>
# <pre><code>    -Can use numpy where() to apply if-then-else
# </code></pre>
# <p><code>df["logic"] = np.where(df["AAA"] &gt; 5, "high", "low")</code>  </p>
# <pre><code>    -Split the frame under condition
# </code></pre>
# <p><code>df[df.AAA &lt;= 5]
# df[df.AAA &gt; 5]</code> </p>
# <h2>Building criteria:</h2>
# <pre><code>    -When there is only 1-2 criterias, can be directly contained in df.loc  
#     -Can return a series or just modify the dataframe
# </code></pre>
# <p><code>df.loc[(df["BBB"] &lt; 25) &amp; (df["CCC"] &gt;= -40), "AAA"]
# df.loc[(df["BBB"] &gt; 25) | (df["CCC"] &gt;= 75), "AAA"] = 0.1</code>   </p>
# <pre><code>    -When there is a list of criteria, it can be done with a list of dynamically built criteria
# </code></pre>
# <p><code>Crit1 = df.AAA &lt;= 5.5
# Crit2 = df.BBB == 10.0
# Crit3 = df.CCC &gt; -40.0
# CritList = [Crit1, Crit2, Crit3]
# AllCrit = functools.reduce(lambda x, y: x &amp; y, CritList)
# df[AllCrit]</code> </p>

# In[ ]:


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.4
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ### Author: Houyu Jiang
# ### Email: houyuj@umich.edu

# + [Topic: pd.diff()](#Topic:-pd.diff()) 
# + [Direction of the difference](#Direction-of-the-difference)
# + [Distance of difference](#Distance-of-difference)

# ## Topic: pd.diff()
#
# - ```pd.diff()``` is a pandas method that we could use to
# compute the difference between rows or columns in DataFrame.
# - We could import it through ```import pandas as pd```.
# - Suppose ```df``` is a pandas DataFrame, we could use 
# ```diff``` method to compute.

df = pd.DataFrame({'a': [1, 2, 3, 4, 5, 6],
                   'b': [1, 1, 2, 3, 5, 8],
                   'c': [1, 4, 9, 16, 25, 36]})
df.diff(axis=0)

# ## Direction of the difference
# - ```pd.diff()``` by default would calculate the 
# difference between different rows.
# - We could let it compute the difference between 
# previous columns by setting ```axis=1```

df.diff(axis=1)

# ## Distance of difference
# - ```pd.diff()``` by default would calculate the difference
# between this row/column and previous row/column
# - We could let it compute the difference between this row/column
# and the previous n row/column by setting ```periods=n```

df.diff(periods=3)


# In[ ]:


# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
# Add a bullet for each topic and link to the level 2 title header using 
# the exact title with spaces replaced by a dash. 
#
# + [Missing Data](#Missing-Data)

# ## Missing Data
# I will be looking at how pandas dataframes handle missing values.
# **Stefan Greenberg**
#
# sfgreen@umich.edu


# ## Imports
import numpy as np
import pandas as pd
# ## Detecting missing data
# - missing data includes `NaN`, `None`, and `NaT`
#     - can change settings so that `inf` and -`inf` count as missing
# - `.isna()` returns True wherever there is a missing value
# - `.notna()` returns True wherever there is not a missing value

# +
df = pd.DataFrame([[0.0, np.NaN, np.NaN, 3.0, 4.0, 5.0],
                   [0.0, 1.0, 4.0, np.NaN, 16.0, 25.0]], 
                 index=['n', 'n^2'])

df.append(df.isna())
# -

# ## Filling missing data
#
# - pandas makes it easy to replace missing values intelligently
# - the `.fillna()` method replaces all missing values with a given value
# - the `.interpolate()` method will use neighboring values to fill in gaps
# in data

# +
df_zeros = df.fillna(0)
df_interp = df.copy()

df_interp.loc['n'] = df_interp.loc['n']                     .interpolate(method='linear')
df_interp.interpolate(method='quadratic', axis=1, inplace=True)

df_zeros
#df_interp
# -

# ## Remove missing data with `.dropna()`
#
# - `.dropna()` will remove rows or columns that have missing values
# - set `axis` to determine whether to drop rows or columns
# - drop a row or column if it has any missing values or only if it has 
# entirely missing values by setting `how` to either *'any'* or *'all'*
# - set a minimum number of non-missing values required to drop row/column
# by setting `thresh`
# - specify what labels along other aixs to look at using `subset` i.e. 
# only drop a row if there is a missing value in a subset of the columns 
# or vise versa

# +
drop_cols   = df.dropna(axis=1)
drop_all    = df.dropna(how='all')
drop_thresh = df.dropna(thresh=5)
drop_subset = df.dropna(subset=[0, 1, 5])

print(df, '\n\n', 
      drop_cols.shape, drop_all.shape, drop_thresh.shape, drop_subset.shape)
# -
# ## Math operations with missing data
# - cumulative methods - `.cumsum()` and `.cumprod()` - by default will skip 
# over missing values
# - `.sum()` and `.prod()` treat missing values as identities
#     - `.sum()` treats missing values as zero
#     - `.prod()` treats missing values as one
#


# +
sumprod = df.append(
          df.sum()
            .to_frame()
            .transpose()
            .rename(index={0:'sum'}))

sumprod.append(
        df.prod()
          .to_frame()
          .transpose()
          .rename(index={0:'prod'}))

