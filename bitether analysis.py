#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv('dset/bitcoin_cash_price.csv', index_col=0,parse_dates=True)


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[9]:


df.index


# In[10]:


df['Mprice']=(df['High']+df['Low'])/2


# In[11]:


df


# In[12]:


df.head()


# In[13]:


df.tail()


# In[15]:


df.isna().any()


# In[45]:


df2=pd.read_csv('dset/ethereum_classic_price.csv')
df2.head()


# In[46]:


df2.dtypes


# In[47]:


df2['Date']=pd.to_datetime(df2['Date'])


# In[48]:


df2.dtypes


# In[49]:


df2.set_index('Date',inplace=True)


# In[50]:


df2.info()


# In[51]:


df2.head()


# In[52]:


df2['Mbprice']=(df2['High']+df2['Low'])/2


# In[53]:


df2.head()


# In[54]:


df2.isna().any()


# In[55]:


prices=pd.DataFrame(index=df.index)


# In[56]:


prices.head()


# In[60]:


prices['Ether']=df2['Mbprice']


# In[61]:


prices['Btc']=df['Mprice']


# In[62]:


prices.head()


# In[63]:


prices.isna().any()


# In[64]:


prices.dtypes


# In[65]:


prices.shape


# In[66]:


prices.info()


# In[67]:


prices.to_csv('Bit-ether-price.csv',encoding='utf-8')


# In[68]:


"""saving a pandas file to csv """


# In[69]:


prices.plot(figsize=(16,9))


# In[70]:


prices.plot(y='Btc', figsize=(12,6))


# In[72]:


prices.plot(y='Ether', figsize=(12,6))


# In[78]:


prices.loc['2018-2-20':'2018-1-10'].plot(y='Btc', figsize=(12,6))


# In[79]:


prices.tail(10)


# In[80]:


"""
equating null values of graphs
df_na=df.loc['2018-1-10':'2018-7-10']
df_na['Ether'].isna().any()
checking the respective time
df_na.loc[df_na['Ether'].isna()]
"""


# In[82]:


prices.loc['2018-2-1':'2017-11-10'].isna()


# In[83]:


"""FIlling the missing values
df.loc['2018-1-11':'2017-12-20'].fillna(method='bfill')
df.fillna(method='bfill', inplace=True)
dropping outlier values from the table
df_clean=df.drop(pd.to_datetime(['2017-11-1','2018-1-1']))
"""


# # Central tendencies for analysis

# In[84]:


prices.mean()


# In[85]:


prices.median()


# # Visualizing distribution

# In[95]:


prices.plot(kind='hist', y='Ether',bins=150)


# In[96]:


prices.plot(kind='hist', y='Btc', bins=150)


# In[98]:


fig, ax=plt.subplots(figsize=(12,6))
sns.distplot(prices['Ether'], ax=ax)


# In[101]:


fig, ax=plt.subplots(figsize=(12,6))
sns.distplot(prices['Btc'],rug=True, ax=ax)


# In[102]:


"""Seaeborns distplot is a general method that will plot a histogram, rugplot and KDE

We can also visualize a cumulative graph of our distribution"""


# In[103]:


fig, ax=plt.subplots(figsize=(12,6))
sns.distplot(prices['Btc'], ax=ax, hist_kws=dict(cumulative=True), kde_kws=dict(cumulative=True))


# In[104]:


fig, ax=plt.subplots(figsize=(12,6))
sns.distplot(prices['Ether'], ax=ax, hist_kws=dict(cumulative=True), kde_kws=dict(cumulative=True))


# This plot shows how many samples fall behind a given value and we can increase the number of bins in order to have more detail

# In[105]:


fig, ax=plt.subplots(figsize=(12,6))
sns.distplot(prices['Ether'], ax=ax, bins=50, hist_kws=dict(cumulative=True), kde_kws=dict(cumulative=True))


# # Visualizing bivariate distributions

# In[106]:


"""The most common way to observe a bivariate distribution is a scatterplot, the jointplot will also include the distribution of the variables:"""


# In[108]:


sns.jointplot(x="Btc", y="Ether", data=prices, height=9)


# In[109]:


"""If you want only a scatter plot, you can use the regplot method, that also fits a linear regression model in the plot:"""


# In[110]:


fig, ax=plt.subplots(figsize=(12,6))
sns.regplot(x="Btc", y="Ether", data=prices, ax=ax)


# # Percentiles

# In[111]:


fig, ax = plt.subplots(figsize=(15, 7))
sns.distplot(prices['Btc'], ax=ax, bins=50,
             hist_kws=dict(cumulative=True),
             kde_kws=dict(cumulative=True))
ax.axhline(0.5, color='red')
ax.axvline(prices['Btc'].median(), color='red')


# In[ ]:




