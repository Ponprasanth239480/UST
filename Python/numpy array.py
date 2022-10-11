#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
arr = np.arange(1,37).reshape(6,6)
arr


# In[2]:


arr[2,1:5]


# In[3]:


arr[1:5,1:5]


# In[4]:


arr_1 = np.arange(10)
print(arr_1)
rev_arr = np.flipud(arr_1)
print(rev_arr)


# In[5]:


arr = np.arange(1,37).reshape(6,6)
arr
rev_arr1 = np.flipud(arr)
print(rev_arr1)
rev_arr2 = np.fliplr(arr)
print(rev_arr2)
rev_arr3 = np.flip(arr)
print(rev_arr3)


# In[6]:


np.ones((3,6),dtype = 'float32')


# In[7]:


np.zeros((3,6),dtype = 'float32')


# In[8]:


np.identity(5)


# In[9]:


np.identity((5),dtype = 'int8')


# In[10]:


arr_2 = np.empty(6)
arr_2


# In[11]:


arr_2.fill(6.0)
arr_2


# In[12]:


np.full(10,6.5)


# In[13]:


np.linspace(0,1,11)


# In[14]:


np.linspace(0,10,12).reshape(4,3)


# In[15]:


np.logspace(0,1,6,base=10)


# In[16]:


exp_1 = np.arange(1,101).reshape(10,10)

exp_1.fill(1)
exp_1[1:-1,1:-1] = 0
exp_1


# In[17]:


exp_2 = np.zeros((10,10),dtype = 'int8')
exp_2[1:-1,1:-1]=1
exp_2


# In[18]:


exp_3 = np.zeros((8,8),dtype = 'int8')
exp_3[1::2,::2] = 1
exp_3[::2,1::2] = 1
exp_3


# In[19]:


arr_3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr_3


# In[20]:


arr_3.sum()


# In[21]:


arr_3.sum(axis=0)


# In[22]:


arr_3.sum(axis=1)


# In[23]:


arr_4 = np.arange(0,36).reshape(6,6)
arr_4


# In[24]:


arr_4.min()


# In[25]:


arr_4.min(axis = 1)


# In[26]:


arr_4.min(axis = 0)


# In[27]:


np.where(arr_4>20)


# In[28]:


np.where(arr_4 == arr_4.min())


# In[29]:


np.where(arr_4 == arr_4.min())[0][0], np.where(arr_4 == arr_4.min())[1][0]


# In[30]:


arr_5 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
arr_5.mean()


# In[31]:


arr_5.mean(axis = 0)


# In[32]:


arr_5.mean(axis = 1)


# In[33]:


np.std(arr_5)


# In[34]:


np.var(arr_5)


# In[35]:


np.average(arr_5, weights = [1,2], axis = 0)


# In[36]:


np.average(arr_5, axis = 0)


# In[37]:


a = np.ones((3,5))
a


# In[38]:


b = np.ones((5))
b


# In[39]:


a+b


# In[40]:


a = np.random.randint(10,20,size=(3,5))
a


# In[41]:


b = np.ones(5,)
b = b.reshape(1,5)
b


# In[42]:


a+b


# In[43]:


b = np.ones((5,1))
b


# In[44]:


a+b


# In[45]:


b = np.ones((5,1))
b1 = b.T
b1


# In[46]:


a+b1


# In[55]:


c = np.random.randint(10,50,size = (5,3))
c


# In[49]:


a.flatten()


# In[50]:


a.ravel()


# In[53]:


arr = np.arange(15)
arr


# In[57]:


num = (arr>3)&(arr<8)
arr[num]*= -1
arr


# In[ ]:




