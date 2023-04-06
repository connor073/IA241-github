#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install xlrd')


# In[2]:


import pandas as pd


# In[3]:


df = pd.read_excel('s3://connor-hicks-241-2023/Diamonds.xls')

df.head()


# In[4]:


df.tail()


# In[5]:


df.describe()


# In[6]:


df['PRICE']


# In[7]:


df['WEIGHT']


# In[8]:


df['RATER']


# In[9]:


df[0:5]


# In[10]:


df[:10]


# In[11]:


df.loc[df['PRICE'] > 1500]


# In[12]:


df['COLOR'].count()


# In[ ]:





# In[14]:


df['COLOR'].value_counts()


# In[15]:


df.mean()


# In[16]:


df['WEIGHT'].min()


# In[19]:


df.groupby('CLARITY').mean()['PRICE']


# In[20]:


df['unit_price'] = df['PRICE'] / df['WEIGHT']

df.head()


# In[21]:


from scipy import stats


# In[22]:


model = stats.linregress(df['WEIGHT'],df['PRICE'])


# In[23]:


print(model.slope)
print(model.intercept)


# In[24]:


print(0.5 * model.slope + model.intercept)


# In[25]:


get_ipython().system('pip install textblob')


# In[26]:


from textblob import TextBlob


# In[28]:


result = TextBlob('i hate dogs')

print(result.sentiment.polarity)


# In[ ]:




