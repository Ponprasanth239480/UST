#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
arr = np.arange(1,37).reshape(6,6)
arr


# In[6]:


arr[2,1:5]


# In[9]:


arr[1:5,1:5]


# In[12]:


arr_1 = np.arange(10)
print(arr_1)
rev_arr = np.flipud(arr_1)
print(rev_arr)


# In[13]:


arr = np.arange(1,37).reshape(6,6)
arr
rev_arr1 = np.flipud(arr)
print(rev_arr1)
rev_arr2 = np.fliplr(arr)
print(rev_arr2)
rev_arr3 = np.flip(arr)
print(rev_arr3)


# In[15]:


np.ones((3,6),dtype = 'float32')


# In[16]:


np.zeros((3,6),dtype = 'float32')


# In[17]:


np.identity(5)


# In[18]:


np.identity((5),dtype = 'int8')


# In[20]:


arr_2 = np.empty(6)
arr_2


# In[23]:


arr_2.fill(6.0)
arr_2


# In[24]:


np.full(10,6.5)


# In[26]:


np.linspace(0,1,11)


# In[28]:


np.linspace(0,10,12).reshape(4,3)


# In[29]:


np.logspace(0,1,6,base=10)


# In[41]:


exp_1 = np.arange(1,101).reshape(10,10)

exp_1.fill(1)
exp_1[1:-1,1:-1] = 0
exp_1


# In[45]:


exp_2 = np.zeros((10,10),dtype = 'int8')
exp_2[1:-1,1:-1]=1
exp_2


# In[50]:


exp_3 = np.zeros((8,8),dtype = 'int8')
exp_3[1::2,::2] = 1
exp_3[::2,1::2] = 1
exp_3


# In[55]:


arr_3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr_3


# In[56]:


arr_3.sum()


# In[57]:


arr_3.sum(axis=0)


# In[58]:


arr_3.sum(axis=1)


# In[60]:


arr_4 = np.arange(0,36).reshape(6,6)
arr_4


# In[62]:


arr_4.min()


# In[63]:


arr_4.min(axis = 1)


# In[64]:


arr_4.min(axis = 0)


# In[69]:


np.where(arr_4>20)


# In[70]:


np.where(arr_4 == arr_4.min())


# In[71]:


np.where(arr_4 == arr_4.min())[0][0], np.where(arr_4 == arr_4.min())[1][0]


# In[75]:


arr_5 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr_5.mean()


# In[76]:


arr_5.mean(axis = 0)


# In[77]:


arr_5.mean(axis = 1)


# In[78]:


np.std(arr_5)


# In[79]:


np.var(arr_5)


# In[80]:


np.average(arr_5, weights = [1,2], axis = 0)


# In[81]:


np.average(arr_5, axis = 0)


# In[83]:


a = np.ones((3,5))
a


# In[85]:


b = np.ones((5))
b


# In[86]:


a+b


# In[88]:


a = np.random.randint(10,20,size=(3,5))
a


# In[90]:


b = np.ones(5,)
b = b.reshape(1,5)
b


# In[91]:


a+b


# In[100]:


b = np.ones((5,1))
b


# In[101]:


a+b


# In[99]:


b = np.ones((5,1))
b1 = b.T
b1


# In[102]:


a+b1


# In[104]:





# In[ ]:




