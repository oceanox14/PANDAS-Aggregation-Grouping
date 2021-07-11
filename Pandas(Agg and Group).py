#!/usr/bin/env python
# coding: utf-8

# __*PANDAS-Aggregation & Grouping*__

# __aggregation__

# count()
# mean() - ortalama
# min()
# max()
# median() - 
# sum() - toplama
# std() - standart sapma
# var() - varyansı

# In[1]:


import seaborn as sns


# In[5]:


df = sns.load_dataset("planets")


# In[7]:


df


# In[9]:


df.head()


# In[11]:


df.shape


# In[12]:


df.mean()


# In[13]:


df["distance"].mean()


# In[14]:


df["mass"].count()


# In[16]:


df["distance"].min()


# In[17]:


df["distance"].max()


# In[18]:


df["mass"].sum()


# In[19]:


df.describe()


# In[20]:


df.describe().T


# __Grouping__

# In[22]:


import pandas as pd


# In[24]:


df = pd.DataFrame({'gruplar': ['A', 'B', 'C', 'A','B', 'C'], 'veri': [10,11,53,23,43,55]}, columns = ['gruplar','veri'])
df


# In[25]:


df.groupby("gruplar")


# In[26]:


df.groupby("gruplar").mean()


# In[27]:


df.groupby("gruplar").sum()


# In[29]:


import seaborn as sns
df20= sns.load_dataset("planets")
df20


# In[30]:


df20.head()


# In[32]:


df20.groupby("method")["orbital_period"].mean()


# In[33]:


df20.groupby("method")["orbital_period"].describe()


# __##İleri Toplulaştırma İşlemleri (Aggregate, filter, transform, apply)__

# 
