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


# In[8]:


def summation(*args):
    return sum(args)
list1 = [10,20,30,40,50]
print(summation(*list1))


# In[9]:


list_1 = [1,2,3,4,5]
list2 = [11,12,13,14,15]
list3 = [10,20,30,40,50]
list4 = [100,200,300,400,500]

print(summation(*list_1,*list2,*list3,*list4))


# write a program to take user dtais and display output as key & values

# In[10]:


def userdetails(*args):
    print(args)

userdetails('prasanth',1404127,641027,'tamilnadu','coimbatore')
    


# In[16]:


def userdetails(**kwargs):
    print(kwargs)

userdetails(name = 'prasanth',ID =1404127,pincode=641027,state='tamilnadu',city='coimbatore')


# In[17]:


def userdetails(**kwargs):
    for key,value in kwargs.items():
        print("{}:{}".format(key,value))
userdetails(name = 'prasanth',ID =1404127,pincode=641027,state='tamilnadu',city='coimbatore')


# program with *args, **kwargs and default values

# In[28]:


def userdetails(licenseno,*args,contact=0,**kwargs):
    print('Licence No : ',licenseno)
    j=''
    for i in args:
        j=j+i
        print('full name : ',j)
        print('Contact number : ',contact)
    for key,val in kwargs.items():
        print('{}:{}'.format(key,val))
name = ['pon','prasanth']
mydict = {'name' : 'prasanth','ID' :1404127,'pincode':641027,'state':'tamilnadu','city':'coimbatore'}
userdetails('DL548792',*name,contact = 5484531564,**mydict)

        
        


# In[29]:


addition = lambda a : a + 10
print(addition(10))


# In[30]:


product = lambda a ,b: a * b
print(product(10,20))


# In[33]:


result = (lambda *args : sum(args))
result(10,20),result(10,20,30),result(10,20,30,40)

