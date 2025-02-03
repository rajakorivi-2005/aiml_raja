#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data1 = pd.read_csv("NewspaperData.csv")
print(data1)


# In[3]:


data1.tail()


# In[4]:


data1.isnull().sum()


# In[5]:


data1.describe()


# In[6]:


#Boxplot for daily column
plt.figure(figsize=(6,3))
plt.title("Box plot for Daily Sales")
plt.boxplot(data1["daily"], vert=False)
plt.show()


# In[7]:


sns.histplot(data1['daily'], kde = True,stat='density',)
plt.show()


# # Observation
# - # There are no missing values
# - # The daily column values appears to be right-skewed
# - # The sunday column values also appear to be right-skewed
# - # There are two outliersin both daily column and also in sunday column and also in sunday as observed from the boxplots

# In[8]:


x = data1["daily"]
y = data1["sunday"]
plt.scatter(data1["daily"], data1["sunday"])
plt.xlim(0, max(x) + 100)
plt.ylim(0, max(y) + 100)
plt.show()


# In[9]:


data1["daily"].corr(data1["sunday"])


# In[10]:


data1[["daily","sunday"]].corr()


# # Observations
# - # The relationship between x (daily) and (sunday) is seen to be linear as seen from scatter plot
# - # The correlation is strong positive with Pearson's correlation coefficient of 0.958154

# In[15]:


import statsmodels.formula.api as smf
model1 = smf.ols("sunday~daily",data = data1).fit()


# In[16]:


model1.summary()


# In[19]:


x = data1["daily"].values
y = data1["sunday"].values
plt.scatter(x, y, color = "m", marker = "o", s = 30)
b0 = 13.84
b1 =1.33
# predicated response vector
y_hat = b0 + b1*x

# plotting the regression line
plt.plot(x, y_hat, color = "g")

# putting Labels
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[20]:


sns.regplot(x="daily", y="sunday", data=data1)
plt.xlim([0,1250])
plt.show()


# In[23]:


# predict sunday sales f0r 200 and 300 and 1500 daily circulation
newdata=pd.Series([200,300,1500])


# In[24]:


data_pred=pd.DataFrame(newdata,columns=['daily'])
data_pred


# In[25]:


model1.predict(data_pred)


# In[26]:


# Predict on all given training data
pred = model1.predict(data1["daily"])
pred


# In[28]:


# Add predicated values as a column in data1
data1["Y_hat"] = pred
data1


# In[29]:


data1["residuals"]= data1["sunday"]-data1["Y_hat"]
data1


# In[31]:


# Compute Mean Squared Error for the model
mse = np.mean((data1["daily"]-data1["Y_hat"])**2)
rmse = np.sqrt(mse)
print("MSE: ",mse)
print("RMSE: ",rmse)


# In[32]:


# Compute Mean Absolute Error (MAE)
mae = np.mean(np.abs(data1["daily"]-data1["Y_hat"]))
mae


# In[33]:


plt.scatter(data1["Y_hat"], data1["residuals"])


# In[ ]:




