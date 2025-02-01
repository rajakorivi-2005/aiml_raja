#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[11]:


data1 = pd.read_csv("NewspaperData.csv")
print(data1)


# In[12]:


data1.tail()


# In[13]:


data1.isnull().sum()


# In[14]:


data1.describe()


# In[15]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert=False)
plt.show()


# In[16]:


sns.histplot(data1['daily'], kde = True,stat='density',)
plt.show()


# # Observation
# - # There are no missing values
# - # The daily column values appears to be right-skewed
# - # The sunday column values also appear to be right-skewed
# - # There are two outliersin both daily column and also in sunday column and also in sunday as observed from the boxplots

# In[19]:


x = data1["daily"]
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[20]:


data1["daily"].corr(data1["sunday"])


# In[21]:


data1[["daily","sunday"]].corr()


# # Observations
# - # The relationship between x (daily) and (sunday) is seen to be linear as seen from scatter plot
# - # The correlation is strong positive with Pearson's correlation coefficient of 0.958154

# In[24]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily",data = data).fit()


# In[25]:


model1.summary()


# In[ ]:




