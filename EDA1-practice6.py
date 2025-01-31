#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Load the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv("data_clean.csv")
print(data)


# In[3]:


data.tail()


# In[4]:


data.info()


# In[5]:


data


# In[6]:


print(type(data))
print(data.shape)


# In[7]:


data.shape


# In[8]:


data.dtypes


# In[9]:


data1 = data.drop(['Unnamed: 0', 'Temp C'], axis = 1)
data1


# In[10]:


data1.info()


# In[11]:


data1['Month'] = pd.to_numeric(data['Month'], errors = 'coerce')
data1.info()


# In[12]:


data1[data1.duplicated()]


# In[13]:


data1[data1.duplicated(keep = False)]


# In[14]:


data1.rename({'Solar.R' : 'Solar','Temp':"Temperature"}, axis=1, inplace = True)
data1


# In[15]:


#Display data1 missing values count in each column using isnull().sum()
data1.isnull().sum()


# In[16]:


#Visualize data1 missing values using graph
cols = data1.columns
colours = ['Black', 'Yellow']
sns.heatmap(data1[cols].isnull(),cmap=sns.color_palette(colours),cbar = True)


# In[17]:


median_ozone = data1["Ozone"].median()
mean_ozone = data1["Ozone"].mean()
print("Median of Ozone: ", median_ozone)
print("Mean of Ozone: ", mean_ozone)


# In[18]:


#Replace the Ozone missing values with median values
data1['Ozone'] = data1['Ozone'].fillna(median_ozone)
data1.isnull().sum()


# In[19]:


median_solar = data1["Solar"].median()
mean_solar = data1["Solar"].mean()
print("Median of Solar: ", median_solar)
print("Mean of Solar: ", mean_solar)


# In[20]:


data1['Solar'] = data1['Solar'].fillna(median_solar)
data1.isnull().sum()


# In[21]:


# Find the mode values of categorical column (weather)
print(data1["Weather"].value_counts())
mode_weather = data1["Weather"].mode()[0]
print(mode_weather)


# In[22]:


print(data1["Month"].value_counts())
mode_month = data1["Month"].mode()[0]
print(mode_month)


# In[23]:


data1.tail()


# In[24]:


# Reset the index column
data1.reset_index(drop=True)


# In[25]:


#Create a figure with two subplots, stacked vertically
fig, axes = plt.subplots(2,1, figsize=(8,6), gridspec_kw={'height_ratios' : [1,3]})

#Plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Ozone"], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Ozone Levels")

#Plot the histogram with KDE curve in the second (bottom) subplot
sns.histplot(data1["Ozone"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Ozone Levels")
axes[1].set_ylabel("Frequency")

#Adjust layout for better spacing
plt.tight_layout()

#Show the plot
plt.show()


# In[26]:


# Create a figure for violin plot
sns.violinplot(data=data1["Ozone"], color='lightgreen')
plt.title("violin Plot")


# In[27]:


#Create a figure with two subplots, stacked vertically
fig, axes = plt.subplots(2,1, figsize=(8,6), gridspec_kw={'height_ratios' : [1,3]})

#Plot the boxplot in the first (top) subplot
sns.boxplot(data=data1["Solar"], ax=axes[0], color='skyblue', width=0.5, orient = 'h')
axes[0].set_title("Boxplot")
axes[0].set_xlabel("Solar Levels")

#Plot the histogram with KDE curve in the second (bottom) subplot
sns.histplot(data1["Solar"], kde=True, ax=axes[1], color='purple', bins=30)
axes[1].set_title("Histogram with KDE")
axes[1].set_xlabel("Solar Levels")
axes[1].set_ylabel("Frequency")

#Adjust layout for better spacing
plt.tight_layout()

#Show the plot
plt.show()


# In[28]:


# Create a figure for violin plot
sns.violinplot(data=data1["Solar"], color='lightgreen')
plt.title("violin Plot")


# In[29]:


plt.figure(figsize=(6,2))
boxplot_data = plt.boxplot(data1["Ozone"], vert=False)
[item.get_xdata() for item in boxplot_data['fliers']]


# In[30]:


data1["Ozone"].describe()


# In[31]:


mu = data["Ozone"].describe()[1]
sigma = data1["Ozone"].describe()[2]

for x in data1["Ozone"]:
    if ((x < (mu - 3*sigma)) or (x > (mu + 3*sigma))):
        print(x)


# In[32]:


import scipy.stats as stats

plt.figure(figsize=(8, 6))
stats.probplot(data1["Ozone"], dist="norm", plot=plt)
plt.title("Q-Q Plot for Outlier Detection", fontsize=14)
plt.xlabel("Theoretical Quantiles", fontsize=12)


# #Observatiions from Q-Q plot
# - The data does not follow normal distribution as the data points are deviating significantly away from the red line
# - The data shows a right-skewed distribution and possible outliers

# #Other visualisations that could help in the detecion of outliers

# In[33]:


data1.info()


# In[34]:


data1_numeric = data1.iloc[:,[0,1,2,6]]
data1_numeric


# In[35]:


data1_numeric.corr()


# #Observations
# - #the highest correlation strength is observed Ozone and -Temperature (0.597087)
# - #the next higher correlation strength is observed between Ozone and wind (-0.523738)
# - #the next correlation strength is observed between wind and temp (-0.441228)
# - #the least correlation strength is observed between solar and wind (-0.055874)

# In[36]:


sns.pairplot(data1_numeric)


# In[37]:


data2=pd.get_dummies(data1, columns=['Month','Weather'])
data2


# #Normalization of the data

# In[38]:


data1_numeric.values


# In[39]:


from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

array = data1_numeric.values

scaler = MinMaxScaler(feature_range=(0,1))
rescaledX = scaler.fit_transform(array)

#transformed data
set_printoptions(precision=2)
print(rescaledX[0:10,:])


# In[41]:


from sklearn.preprocessing import StandardScaler

array = data1_numeric.values
scaler = StandardScaler()
rescaledX = scaler.fit_transform(array)

set_printoptions(precision=2)
print(rescaledX[0:10,:])


# In[ ]:




