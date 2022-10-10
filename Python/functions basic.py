#!/usr/bin/env python
# coding: utf-8

# In[1]:


var1 = 100
def myfunc():
    var1 = var1 + 100
    print(var1)
myfunc()
print(var1 + 100)


# In[2]:


var1 = 100
def myfunc():
    var1 = 90
    return var1
print(myfunc())
print(var1)


# In[3]:


def summation(a,b,c):
    return a+b+c
print(summation(10,20,30))


# In[4]:


print(summation(10,20,30,40))


# In[5]:


def summation(*args):
    return sum(args)
print(summation(10,20,30,40))
print(summation(10,20,30,40,50))
print(summation(10,20,30))
print(summation(10,20))


# In[ ]:




