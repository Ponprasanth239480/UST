#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[3]:


autoprice = pd.read_csv('Automobile_price_data__Raw_.csv', sep = ',')
display(autoprice)


# In[5]:


autoprice.info()


# In[6]:


autoprice.drop(['symboling','normalized-losses'], axis = 1)


# In[8]:


cols = ['bore','stroke','horsepower','peak-rpm','price']
autoprice[cols] = autoprice[cols].apply(pd.to_numeric,args = ('coerce',))


# In[9]:


autoprice.isnull().sum()


# In[ ]:


autoprice.dropna()


# In[10]:


autoprice['price'].plot(kind='line',figsize=(15,8))


# In[11]:


autoprice['price'].sort_values().unique()


# In[14]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(15,9))
plt.plot(autoprice['price'].sort_values().unique(),color = 'teal')


# In[15]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(14,8))
plt.plot(autoprice.sort_values(by = 'price')['price'],autoprice.sort_values(by = 'price')['city-mpg'])
plt.title('price vs city milage line plot')
plt.xlabel('price')
plt.xlabel('city-mpg')


# #### barchart

# In[16]:


sns.set_style('whitegrid')
autoprice[['price']].iloc[10:75,].plot.bar(figsize=(14,8))


# In[17]:


autoprice[['make']].value_counts().plot.bar(figsize=(14,8))


# #### histogram

# In[19]:


fig = plt.figure(figsize=(14,8))
plt.hist(autoprice['price'],bins = 20)
plt.title('price vs frequency histogram plot')
plt.xlabel('price')
plt.xlabel('frequency')
plt.show()


# In[21]:


fig = plt.figure(figsize=(14,8))
sns.distplot(autoprice['price'],bins = 20)
plt.show()


# In[22]:


fig = plt.figure(figsize=(14,8))
sns.distplot(autoprice['price'],bins = 20,color = 'skyblue', hist = False)
plt.show()


# #### subplot

# In[41]:


fig = plt.figure(figsize=(18,6))
plt.subplot(1,2,1)
plt.hist(autoprice[autoprice['num-of-doors']== 'four']['price'],bins=20)
plt.title('price of four door car histogram plot')
plt.xlabel('price of four door car')
plt.ylabel('count of vehicle')

plt.subplot(1,2,2)
plt.hist(autoprice[autoprice['num-of-doors']== 'two']['price'],bins=20,color = 'orangered')
plt.title('price of two door car histogram plot')
plt.xlabel('price of two door car')
plt.ylabel('count of vehicle')

plt.show()


# In[31]:


fig = plt.figure(figsize=(10,7))
sns.scatterplot(x=autoprice['city-mpg'],y=autoprice['price'],marker = 's',color = 'orangered',alpha=0.7)
plt.show()


# In[49]:


body_style = autoprice['body-style'].unique()
body_style


# In[53]:


colors_ = ['crimson','deeppink','lightgreen', 'deepskyblue','darkviolet']
fig = plt.figure(figsize=(20,9))

for index, (style,label) in enumerate (zip(body_style, colors_)):
    plt.subplot(2, 3, index + 1)
    sns.scatterplot(x = autoprice[autoprice['body-style'] == style]['city-mpg'], 
            y = autoprice[autoprice['body-style'] == style]['price'], color = label, marker='s')
plt.show()


# ##### piechart

# In[54]:


autoprice['make'].value_counts()


# In[55]:


plt.style.use('ggplot')
fig = plt.figure(figsize=(20,9))
plt.pie(autoprice['make'].value_counts(), labels = autoprice['make'].value_counts().index, autopct = '%0.0f%%')
plt.show()


# In[56]:


plt.style.use('seaborn-whitegrid')
plt.figure(figsize=(14,6))
sns.countplot(autoprice['make'])
plt.xticks(rotation = 90)
plt.show()


# In[ ]:




