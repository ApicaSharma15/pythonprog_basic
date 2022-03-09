#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python program to find sum of elements in list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("Sum of elements in List",sum(lst))


# In[2]:


#2.	Write a Python program to  Multiply all numbers in the list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
product = 1
for i in lst:
    product = product*i
print("Product of elements in List is :",product)


# In[3]:


#3.	Write a Python program to find smallest number in a list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("The Smallest no. in the list is :",min(lst))


# In[4]:


#4.	Write a Python program to find largest number in a list?

n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
print("The largest no. in the list is :",max(lst))


# In[5]:


#5.	Write a Python program to find second largest number in a list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
lst.sort()
print("The sorted list is ",lst)
print("The second largest number in the list is ",lst[-2])


# In[6]:


#6.	Write a Python program to find N largest elements from a list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)
lst.sort()
print("The sorted list is ",lst)
nlar = int(input("Enter how many largest number you want from list:"))

if n < nlar :
    print("enterted value is larger then the length of list")
else:
    print(nlar,"largest elements from the list are :",lst[(n-nlar):])


# In[7]:


#7.	Write a Python program to print even numbers in a list?
lent =  int(input("Enter  the len of the list :"))
lst = []
for i in  range(lent):
  lst.append(int(input()))
print("The List is :" ,lst)
even = [i for i in lst if i%2==0 ]
print("The even numbers in list" , even)


# In[8]:


#8.	Write a Python program to print odd numbers in a List?
lent =  int(input("Enter  the len of the list :"))
lst = []
for i in  range(lent):
  lst.append(int(input()))
print("The List is :" ,lst)
odd = [i for i in lst if i%2 != 0 ]
print("The even numbers in list" , odd)


# In[10]:


#9.	Write a Python program to Remove empty List from List?
lst = [55,[],14,75,[],96,80,[],36]
print("The List :",lst)
new_list = [item for item in lst if item != []]
print("The list after removing empty lists :" , new_list)


# In[11]:


#10.	Write a Python program to Cloning or Copying a list?
n = int(input("Enter the lenth of your list : "))
lst = []

for i in range(n):
    lst.append(int(input()))
print("The List is ",lst)

lst_copy = lst.copy()
print("Cloning By list copying lst ",lst_copy)


# In[12]:


#11.	Write a Python program to Count occurrences of an element in a list?

lent = int(input("Enter the lenth of your list : "))
lst = []

for i in range(lent):
    lst.append(int(input()))
print("The List is ",lst)
ele= int(input("Enter the element to find its occurance : "))
print(ele,"has occured {} times in the list ".format(lst.count(ele)))


# In[ ]:




