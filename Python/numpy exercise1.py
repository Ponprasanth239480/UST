#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[12]:


ex = np.random.randint(10,50,size = 20)
print(ex)


# In[13]:


ex[ex%2==1] *= -1          # select & multiply only odd indexes, don't effect even ones

print (ex)


# In[14]:


ex1 = np.random.randint(10,50,size = 20)
print(ex1)
ex1[ex1%2==0] *= -1          # select & multiply only odd indexes, don't effect even ones

print (ex1)


# In[17]:


iris_data = np.genfromtxt('iris.csv',delimiter = ',', skip_header = 1, dtype = str, usecols = [0,1,2,3,4])
iris_data


# In[18]:


iris_data = np.genfromtxt('iris.csv',delimiter = ',', skip_header = 1, dtype = str, usecols = [4])
np.unique(iris_data, return_counts = True)


# In[19]:


iris_data = np.genfromtxt('iris.csv',delimiter = ',', skip_header = 1, dtype = float, usecols = [0,1,2,3])
iris_data


# In[20]:


iris_data[(iris_data[:,2]>1.5)&(iris_data[:,0]<5.0)]


# In[21]:


np.isnan(iris_data)


# In[22]:


np.isnan(iris_data).any()


# In[23]:


iris_data[(iris_data[:, 2] > 3.4) & (iris_data[:, 0] < 1.7)]


# In[30]:


iris_data[(iris_data[:, :] == 3.4) | (iris_data[:, :] == 1.7)] = np.nan
iris_data


# In[31]:


np.isnan(iris_data)


# In[33]:


np.isnan(iris_data).sum(axis = 0)


# In[55]:


iris_data = np.genfromtxt('iris.csv',delimiter = ',', skip_header = 1, dtype = float, usecols = [0,1,2,3])
for i in range (iris_data.shape[1]):
    values,count = np.unique(iris_data[:,i], return_counts = True)
    print(values[np.argmax(count)])


# In[58]:


iris_data = np.genfromtxt('iris.csv',delimiter = ',', skip_header = 1, dtype = float, usecols = [0,1,2,3])
for i in range (iris_data.shape[1]):
    print(np.argmax(iris_data[:,i]>2.3))


# In[59]:


for i in range (iris_data.shape[1]):
    print(np.argwhere(iris_data[:,i]>2.3)[0])


# In[64]:


alpha
string=str(input('enter the string'))
for i in string:
    if (i.isalpha()):
        alpha+=1
print("Number of Digit is", len(string)-alpha)
print("Number of Alphabets is", alpha)


# In[73]:


frequency = dict()
alpha,string=0,"Geeks1234"
for i in string:
    if (i.isalpha()):
        alpha+=1
print("digits", len(string)-alpha)
print("letters", alpha)


# In[68]:


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

string1 = str(input("enter the string")).lower()
number_of_words = len(string1.split())
print(number_of_words)
#print(word_count(string1)


# In[77]:


sentence = str(input("enter the string"))
dictionary ={"DIGITS":0, "LETTERS":0}
for character in sentence:
    if character.isdigit():
       dictionary["DIGITS"]+=1
    elif character.isalpha():
       dictionary["LETTERS"]+=1
    else:
        pass
print(dictionary)


# In[83]:


fileobj = open ("poem.txt")
fileobj = open ("poem.txt",'r')
poem = list[fileobj.read()]
print(poem)


# In[90]:


with open ("poem.txt",'r') as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)


# In[93]:


a = {}
with open("poem.txt") as f:
    for line in f:
       (k, v) = line.split()
       a[str(k)] = v
print(a)


# In[105]:


import pandas as pd
text = open("poem.txt", "r")
  
d = dict()  
for line in text:
    line = line.strip()
    line = line.lower()
    words = line.split(" ")
                         
  
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
print (d)
pd.Series(d).plot.bar()


# In[ ]:




