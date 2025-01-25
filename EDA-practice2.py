#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[5]:


data.tail()


# In[6]:


data.info()


# In[7]:


data


# In[8]:


print(type(data))
print(data.shape)


# In[9]:


data.shape


# In[10]:


data.dtypes


# In[11]:


data1 = data.drop(['Unnamed: 0', 'Temp C'], axis = 1)
data1


# In[12]:


data1.info()


# In[13]:


data1['Month'] = pd.to_numeric(data['Month'], errors = 'coerce')
data1.info()


# In[14]:


data1[data1.duplicated()]


# In[15]:


data1[data1.duplicated(keep = False)]


# In[17]:


data1.rename({'Solar.R' : 'Solar','Temp':"Temperature"}, axis=1, inplace = True)
data1


# In[18]:


#Display data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[24]:


#Visualize data1 missing values using graph
cols = data1.columns
colours = ['Black', 'Yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar = True)


# In[25]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[29]:


#Replace the Ozone missing values with median values
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[30]:


median_solar = data1["Solar"].median()
mean_solar = data1["Solar"].mean()
print("Median of Solar: ", median_solar)
print("Mean of Solar: ", mean_solar)


# In[31]:


data1['Solar'] = data1['Solar'].fillna(median_solar)
data1.isnull().sum()


# In[ ]:




