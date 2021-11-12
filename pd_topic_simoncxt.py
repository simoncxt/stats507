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




