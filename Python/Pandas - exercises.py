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


# In[4]:


series_country = pd.Series(np_country)
series_country


# In[5]:


data_series = {"column1" : pd.Series([10,20,30,40,50]),
               "column2" : pd.Series([100,200,300,400,500])
              }
print(data_series)


# In[6]:


pd.DataFrame(data_series)


# In[7]:


country_happiness = pd.Series([7.809, 7.646, 7.560, 7.504, 7.488, 7.449, 7.353, 7.3, 7.294, 7.238],
                             index = ['Finland','Denmark','Switzerland','Iceland','Norway',
                                      'Netherlands','Sweden','NewZealand','Austria','Luxembourg'])
country_happiness


# In[8]:


country_happiness.index


# In[9]:


country_happiness.values


# In[10]:


country_happiness[0:5]


# In[11]:


autoprice = pd.read_csv('Automobile_price_data__Raw_.csv')
display(autoprice)


# In[12]:


autoprice.head()


# In[13]:


autoprice.tail()


# In[14]:


autoprice.shape


# In[15]:


autoprice.columns


# In[16]:


for i,j in autoprice.iterrows():
    print(i,j)


# In[17]:


autoprice.info()


# In[18]:


autoprice.isnull()


# In[19]:


autoprice.isnull().sum()


# In[20]:


autoprice_1 = autoprice.replace('?' , np.nan)
autoprice_1


# In[21]:


autoprice_1.isnull().sum()


# In[22]:


autoprice['engine-size'].sort_values()


# In[23]:


autoprice.sort_values(by = 'engine-size', ascending = True)


# In[24]:


autoprice.sort_values(by = 'city-mpg', ascending = False)


# In[25]:


autoprice['engine-size'].unique()


# In[26]:


autoprice[['engine-size','city-mpg','make']]


# In[28]:


autoprice['make'] == 'audi'


# In[27]:


autoprice[autoprice['make'] == 'audi']


# In[34]:


autoprice[(autoprice['make'] == 'audi')&(autoprice['num-of-doors'] == 'two')]


# In[35]:


autoprice[(autoprice['make'] == 'audi')|(autoprice['num-of-doors'] == 'two')]


# In[40]:


autoprice[(autoprice['engine-size'] > 120 )&(autoprice['body-style'] == 'convertible')]


# In[41]:


autoprice.loc[:,:]


# In[42]:


autoprice.loc[10:20,:]


# In[45]:


autoprice.loc[10:20,'make':'engine-size']


# In[46]:


autoprice.iloc[10:20,2:9]


# In[47]:


autoprice.iloc[10:20,::-1]


# In[52]:


df_rand = autoprice.sample(n = 10)
df_rand


# In[51]:


df_rand = autoprice.sample(frac = 0.2)
df_rand


# In[53]:


autoprice.query("make == 'toyota' and `engine-size` > 100 and `drive-wheels` == 'fwd'")


# In[54]:


autoprice.drop([2,3,4,5,6,8,9,10], axis = 0)


# In[55]:


autoprice.drop(['symboling','normalized-losses'], axis = 1)


# In[56]:


autoprice.duplicated()


# In[57]:


autoprice[autoprice.duplicated()]


# In[58]:


autoprice.drop_duplicates(inplace = True)


# In[59]:


autoprice.groupby(['make'])


# In[61]:


autoprice.groupby(['make']).first()


# In[62]:


autoprice.groupby(['make'])[['city-mpg','highway-mpg']].mean().sort_values(by = 'city-mpg')


# In[64]:


autoprice.groupby(['make'])[['city-mpg','highway-mpg']].max().sort_values(by = 'city-mpg')


# In[65]:


autoprice.groupby(['make','body-style'])[['city-mpg','highway-mpg']].max().sort_values(by = 'city-mpg')


# In[66]:


data_series1 = pd.Series([10,20,30,40,50])
data_series2 = pd.Series([100,200,300,400,500])


# In[67]:


pd.concat([data_series1,data_series2], axis = 1)


# In[ ]:




