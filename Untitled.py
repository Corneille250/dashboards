#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd 
df1=pd.read_csv(r'C:\Users\corneille.n\Downloads\Churn_Modelling.csv')
df1


# In[4]:


df1.info()


# In[5]:


df1.columns


# In[7]:


df1.isnull().sum()


# In[9]:


df1.describe()


# In[10]:


df1.describe(include='all')


# In[12]:


df1.Age.describe()


# In[19]:


df1['Geography'].value_counts()


# In[21]:


pd.crosstab(df1['Geography'],df1['Gender'])


# In[22]:


df1.Exited.value_counts()


# In[26]:


Corr=df1.corr(numeric_only='true')
Corr


# In[28]:


df1.dtypes


# In[31]:


df2=df1.drop(["RowNumber","CustomerId","Surname"],axis=1)


# In[32]:


df2


# In[34]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
df2['Gender']=le.fit_transform(df2['Gender'])
df2['Geography']=le.fit_transform(df2['Geography'])


# In[35]:


df2['Geography'].value_counts()


# In[ ]:




