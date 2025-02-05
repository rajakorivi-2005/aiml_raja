#!/usr/bin/env python
# coding: utf-8

# # Assumptions in Multilinear Regression
# - # Linearity: The relationship between the predictors and the response is linear.
# - # Independence: Observatiions are independent of each other.
# - # Homoscedasticity: The residuals (Y - Y_hat) exhibit constant variance at all the levels of the predictor.
# - # Normal Distribution of Errors: The residuals of the model are normally distributed.

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[2]:


# Read the data from csv file
cars = pd.read_csv("Cars.csv")
cars.head()


# In[3]:


cars = pd.DataFrame(cars, columns=["HP","VOL","SP", "WT","MPG"])
cars.head()


# # DESCRIPTION OF COLUMNS
# - # MPG: Mileage of the car (Mile per Gallon) (This is Y-column to be predicted)
# - # HP: Horse Power of the car (X1 column)
# - # VOL: Volume of the car(size) (X2 column)
# - # SP: Top speed of the car (Miles per Hour) (X3 column)
# - # WT: Weight of the car (Pounds) (X4 column)VOL: Volume of the car(size) (X2 column)
# 

# In[4]:


cars.isna().sum()


# In[5]:


cars.info()


# # Observations
# - # There are no missing values
# - # There are 81 observations (81 different cars data)
# - # The data types of the columns are also relevant and valid

# In[8]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

#creating a boxplot
sns.boxplot(data=cars, x='HP', ax=ax_box, orient='h')
ax_box.set(xlabel='')

#creating a histogram in the same x axis
sns.histplot(data=cars, x='HP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

#Adjust layout
plt.tight_layout()
plt.show()


# In[9]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

#creating a boxplot
sns.boxplot(data=cars, x='SP', ax=ax_box, orient='h')
ax_box.set(xlabel='')

#creating a histogram in the same x axis
sns.histplot(data=cars, x='SP', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

#Adjust layout
plt.tight_layout()
plt.show()


# In[10]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

#creating a boxplot
sns.boxplot(data=cars, x='WT', ax=ax_box, orient='h')
ax_box.set(xlabel='')

#creating a histogram in the same x axis
sns.histplot(data=cars, x='WT', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

#Adjust layout
plt.tight_layout()
plt.show()


# In[11]:


fig, (ax_box, ax_hist) = plt.subplots(2, sharex=True, gridspec_kw={"height_ratios": (.15, .85)})

#creating a boxplot
sns.boxplot(data=cars, x='VOL', ax=ax_box, orient='h')
ax_box.set(xlabel='')

#creating a histogram in the same x axis
sns.histplot(data=cars, x='VOL', ax=ax_hist, bins=30, kde=True, stat="density")
ax_hist.set(ylabel='Density')

#Adjust layout
plt.tight_layout()
plt.show()


# # Observations from boxplot and histograms
# - # There are some extreme values (outliers) observed in towards the right tail of SP and HP distributions
# - # In VOL and WT columns, a few outliers are observed in both tails of their distributions.
# - # The extreme values of cars data may have come from the specially designed nature of cars
# - # As this is multi-dimensional data, the outliers with respect to spatial dimensions may have to be considered while building the regression model

# In[12]:


cars[cars.duplicated()]


# In[15]:


# pair plot
sns.set_style(style='darkgrid')
sns.pairplot(cars)


# In[14]:


cars.corr()


# In[16]:


#Build model
#import statsmodels.formula.api as smf
model = smf.ols('MPG~WT+VOL+SP+HP',data=cars).fit()


# In[17]:


model.summary()


# In[ ]:




