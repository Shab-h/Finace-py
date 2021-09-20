#!/usr/bin/env python
# coding: utf-8

# In[1]:


#This is a Sentdex Python Programming for Finace series.
#Part-2
#Website Tutorial Link: https://pythonprogramming.net/getting-stock-prices-python-programming-for-finance/


# In[16]:


import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

style.use('ggplot')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


# In[17]:


#Adding a new column into your dataframe (You could also add some of your own calcs. Less efficicent)
df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
print(df.head())


# In[19]:


#Graphing Multiple grpahs

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=4, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()


# In[ ]:




