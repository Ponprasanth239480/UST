#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


a = pd.Series(list('abcdef'))
a


# In[3]:


np_country = np.array(['luxembourg','Norway','Japan','Switzerland','United States','Qatar','Iceland',
                       'Sweden','Singapore','Denmark'])
np_country


# In[5]:


series_country = pd.Series(np_country)
series_country


# In[7]:


data_series = {"column1" : pd.Series([10,20,30,40,50]),
               "column2" : pd.Series([100,200,300,400,500])
              }
print(data_series)


# In[9]:


pd.DataFrame(data_series)


# In[10]:


country_happiness = pd.Series([7.809, 7.646, 7.560, 7.504, 7.488, 7.449, 7.353, 7.3, 7.294, 7.238],
                             index = ['Finland','Denmark','Switzerland','Iceland','Norway',
                                      'Netherlands','Sweden','NewZealand','Austria','Luxembourg'])
country_happiness


# In[11]:


country_happiness.index


# In[12]:


country_happiness.values


# In[13]:


country_happiness[0:5]


# In[15]:


autoprice = pd.read_csv('Automobile_price_data__Raw_.csv')
display(autoprice)


# In[16]:


autoprice.head()


# In[17]:


autoprice.tail()


# In[18]:


autoprice.shape


# In[20]:


autoprice.columns


# In[21]:


for i,j in autoprice.iterrows():
    print(i,j)


# In[22]:


autoprice.info()


# In[23]:


autoprice.isnull()


# In[24]:


autoprice.isnull().sum()


# In[25]:


autoprice_1 = autoprice.replace('?' , np.nan)
autoprice_1


# In[26]:


autoprice_1.isnull().sum()


# In[28]:


autoprice['engine-size'].sort_values()


# In[27]:


autoprice.sort_values(by = 'engine-size', ascending = True)


# In[30]:


autoprice.sort_values(by = 'city-mpg', ascending = False)


# In[31]:


autoprice['engine-size'].unique()


# In[32]:


autoprice[['engine-size','city-mpg','make']]

