#!/usr/bin/env python
# coding: utf-8

# In[7]:


num = 28
if num %2 == 0:
    print("even")
else:
    print("odd")


# In[9]:


L =[1,9,2,10,56,89]
[x for x in L if x%2 == 0]


# In[10]:


L =[1,9,2,10,56,89]
[x for x in L if x%2 != 0]


# In[16]:


L =[1,9,2,10,56,89]
average = sum(L)/len(L)
print(average)


# In[17]:


d1 = {"Ram":[70,71,98,100], 'John': [56,58,82,95]}
d1

