#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import influence_plot
import numpy as np


# In[2]:


cars = pd.read_csv("Cars.csv")
cars.head()


# In[4]:


cars = pd.DataFrame(cars, columns=["HP","VOL","SP", "WT","MPG"])
cars.head()


# # Description of columns
# - # MPG: Mileage of the car (Mile per Gallon) (This is Y-column to be predicted)
# - # HP: Horse Power of the car (X1 column)
# - # VOL: Volume of the car(size) (X2 column)
# - # SP: Top speed of the car (Miles per Hour) (X3 column)
# - # WT: Weight of the car (Pounds) (X4 column)
# 

# In[5]:


cars.isna().sum()


# In[6]:


cars.info()


# # Observations
# - # There are no missing values
# - # There are 81 observations (81 different cars data)
# - # The data types of the columns are also relevant and valid
# 

# In[ ]:




