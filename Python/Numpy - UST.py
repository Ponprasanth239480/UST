#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
print(arr)


# In[4]:


print(type(arr))


# In[5]:


arr.dtype


# In[6]:


arr.itemsize


# In[7]:


arr.shape


# In[8]:


arr.ndim


# In[9]:


arr.nbytes


# In[10]:


np.arange(1,11)


# In[11]:


np.arange(1,11,2)


# In[14]:


a = np.array([10,20,30,40,50])
b = np.array([1,2,3,4,5])

print(a+b)
print(a*b)
print(a**b)


# In[16]:


import time
import numpy as np
arraysize = 1000000
def python_version():
    t1 = time.time()
    x=range(arraysize)
    y=range(arraysize)
    z=[x[i] + y[i] for i in range(len(x))]
    return time.time()-t1

def numpy_version():
    t1 = time.time()
    x=np.arange(arraysize)
    y=np.arange(arraysize)
    z=x+y
    return time.time()-t1
t1=python_version()
t2=numpy_version()

print('numpy in this example is : ' + str(t1/t2) + 'faster')


# In[17]:


distancearr = np.array([10,20,30,40,50])
timearr = np.array([12,5,14,6,8])
speedarr = distancearr/timearr
speedarr


# In[18]:


distancelist = [10,20,30,40,50]
timelist = [12,5,14,6,8]
speedlist = distancelist/timelist
speedlist


# In[19]:


a = np.array([10,20,30,40,50])
b = np.array([[1,2,3,4,5],
              [10,20,30,40,50]])
print(b)


# In[20]:


b.shape


# In[21]:


b.dtype


# In[22]:


b.ndim


# In[23]:


b[1][3]


# In[25]:


b[-1][-2]


# In[35]:


c = np.array([[[1,2,3,4,5],
              [10,20,30,40,50],
             [11,22,33,44,55]],
             
            [[1,2,3,4,5],
              [10,20,30,40,50],
             [11,22,33,43,55]],
             
            [[1,2,3,4,5],
              [10,20,30,40,50],
             [11,22,33,44,55]]])
print(c)


# In[29]:


c.shape


# In[32]:


c.dtype


# In[33]:


c.ndim


# In[34]:


c.size


# In[39]:


c[1][2][3]


# In[40]:


c[1,2,3]


# In[41]:


a[1] = 5.5
print(a)


# In[45]:


d=a.astype('float32')
print(d.dtype)
print(d)


# In[46]:


d[1] = 5.5
print(d)


# In[ ]:




