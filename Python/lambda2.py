#!/usr/bin/env python
# coding: utf-8

# In[3]:


list2 = [11,12,13,14,15]
def odd (n):
    if (n % 2 == 1):
        return True
    else:
        return False
    
oddnum = list(filter(odd, list2))
print(oddnum)


# In[4]:


odd_num = list(filter(lambda num : num%2 == 1, list2))
odd_num


# In[5]:


doubles = list(map(lambda num : num*2,odd_num))
doubles


# In[6]:


from functools import reduce

def summation(a,b):
    return a + b
sum_all = reduce(summation,doubles)
sum_all


# In[8]:


sum_all=reduce(lambda a,b:a+b,doubles)
sum_all


# In[23]:


from functools import reduce
list3 = [1,2,3,4,5,6,7,8,9]
def even (n):
    if (n % 2 == 0):
        return True
    else:
        return False
def summation(a,b):
    return a + b
    
evennum = list(filter(even, list3))
print(evennum)
cube = list(map(lambda num : num**3,evennum))
print(cube)
sum_all=reduce(lambda a,b:a+b,cube)
print(sum_all)
sumall = reduce(lambda a,b:a+b,list(map(lambda num : num**3,list(filter(even, list3)))))
print(sumall)


# In[14]:


cube = list(map(lambda num : num**3,evennum))
cube


# In[27]:


list4 = [1,2,3,4,5,6,7,8,9,10,11,12]
min_list = reduce(lambda a,b: a if a<b else b,list4)
print(min_list)
max_list = reduce(lambda a,b: a if a>b else b,list4)
max_list


# In[34]:


a =frozenset([10,20,30,40,50])
b =frozenset([30,40,50,60,70])
c = a.copy()
print(c)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))


# In[35]:


list = [x**2 for x in range (1,11) if x%2 == 0]
list


# In[41]:


list1 = []
for x in range(1,11):
    if x%2==0:
        list1.append(x)

list1        


        
    


# In[45]:


python_libs = ['python','math','numpy','pandas','datetime','sys']
upper_python_libs = []
for libs in python_libs:
    upper_python_libs.append(libs.upper())
print(upper_python_libs)


# In[ ]:




