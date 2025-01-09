#!/usr/bin/env python
# coding: utf-8

# In[6]:


greet = lambda name : print(f"Good Morning {name}!")


# In[8]:


greet("Rk")


# In[9]:


product = lambda a,b,c : a*b*c


# In[10]:


product(20,30,40)


# In[11]:


even = lambda L :[x for x in L if x%2 ==0]


# In[13]:


my_list = [100,3,9,38,43,56,20]
even(my_list)


# In[17]:


def mean_value(*n):
    sum = 0
    counter = 0
    for x in n:
        counter = counter +1
        sum += x
    mean = sum /counter
    return mean


# In[18]:


def product(*n):
    result = 1
    for i in range(len(n)):
        result *= n[i]
    return result


# In[20]:


product (2,3,5)

