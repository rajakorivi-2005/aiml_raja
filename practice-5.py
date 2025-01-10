#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np


# In[10]:


x = np.array(["A",40,67,57,90])
print(x)
print(type(x))
print(x.dtype)


# In[13]:


a1 = np.array([3,4,5,8,7,2,8])
print(a1)
a1.dtype


# In[14]:


a2 =np.array([[3,4,6],[7,9,10],[4,6,12]])
a2


# In[15]:


print(a2.sum(axis = 1))
print(a2.sum(axis=0))


# In[16]:


print(a2)
print(np.mean(a2, axis =1))
print(np.mean(a2, axis =0))


# In[18]:


a3 =np.array([[3,4,5],[7,2,8],[9,1,6]])
print(a3)
np.fill_diagonal(a3,0)
print(a3)


# In[ ]:




