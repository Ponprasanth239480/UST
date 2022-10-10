#!/usr/bin/env python
# coding: utf-8

# In[1]:


python_libs = ['python','math','numpy','pandas','datetime','sys']
upper_python_libs = list(map(lambda num : num.upper(),python_libs))
print(upper_python_libs)


# In[6]:


mylist = ['php','madam','python','numpy','class','rewire','salas']
""""
palindrome_list = []
for name in mylist:
    if name == name[::-1]:
        palindrome_list.append(name)
print(palindrome_list)
""""
        
    
    


# In[9]:


palindrome = list(filter(lambda name : name == name[::-1], mylist))
palindrome


# In[11]:


file = open('poem.txt','r')
text= file.read()
if 'star' in text:
    print('star is present')
else:
    print('star is present')
file.close()

    
    


# In[ ]:




