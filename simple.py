#!/usr/bin/env python
# coding: utf-8

# In[1]:


def prime(n):
    for i in range(2,n):
        if n%i==0:
            return "NOT Prime Number"
    else:
        return "Prime Number"
    


# In[2]:


def CA(r):
    return 3.14*r*r


# In[3]:


def mylen(data):
    c=0
    for i in data:
        c+=1
    return c


# In[4]:


def sqrt(n):
    return n**0.5


# In[ ]:




