#!/usr/bin/env python
# coding: utf-8

# # Analyzing Covid19 

# COVID-19 is a contagious respiratory illness.
# 
# Data Source:  [European Centre for Disease Prevention and Control](https://www.ecdc.europa.eu/en/publications-data/download-todays-data-geographic-distribution-covid-19-cases-worldwide)
# 
# Author:  Connor Hicks
# 
# 

# ## Import Data

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


# In[2]:


get_ipython().system('pip install xlrd')


# In[3]:


df = pd.read_excel('s3://connor-hicks-241-2023/covid_data.xls')
df.head()


# ## Number of Cases per Day

# In[7]:


df['dateRep'] = pd.to_datetime(df['dateRep']) #convert to date format

sum_death_by_date = df.groupby('dateRep')['cases'].sum()
sum_death_by_date.plot()


# More cases in November and December.

# In[6]:


sum_death_by_country = df.groupby('countriesAndTerritories')['deaths'].sum()
sum_death_by_country.nlargest(10).plot.bar()


# U.S., Brazil, and India are the top 3 countries in number of deaths.

# In[9]:


pd.unique(df['countriesAndTerritories'])


# ## Select UK Data

# In[17]:


uk_data = df.loc[df['countriesAndTerritories'] == 'United_Kingdom']
uk_data.head() #the top 5 rows


# In[18]:


uk_data.plot.scatter(x='cases',y='deaths',c= 'month')


# Higher death rate in early months, low death rate in later months.

# In[ ]:




