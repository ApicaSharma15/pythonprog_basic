#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Write a Python program to print 'Hello Python'?

print('Hello Python')


# In[5]:


#2. Write a Python program to do arithmetical operations addition and division.?

def add(a,b):
    return a+b

def divide(a,b):
    return a/b


# In[6]:


add(3,5)


# In[7]:


divide(4,5)


# In[8]:


#3. Write a Python program to find the area of a triangle?

base = int(input("Enter the base of Triangle ="))
Height = int(input("Enter the height of Triangle = "))
Area = (Height*base)/2
print("The Area of Triangle of Base {} , Height {} is {}".format(base , Height , Area))


# In[11]:


#4. Write a Python program to swap two variables?
first_variable = int(input("First Variable ="))
second_variable = int(input("Second Variable ="))
print("First Variable Before swap  : {} \n Second variable Before Swap  : {}".format(first_variable,second_variable))
first_variable , second_variable = second_variable , first_variable

print("After Swap : \n First Variabe : {} \n  Second Variable : {}".format(first_variable , second_variable))


# In[12]:


#5. Write a Python program to generate a random number?
import random
print(random.randint(0,6))


# In[ ]:




