#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python Program to find sum of array?
sum =0
arr = [1,2,3,4,5,9]
for i in range(0,len(arr)):
    sum+=arr[i]
print("Sum : ",sum)


# In[2]:


#2.	Write a Python Program to find largest element in an array?
c = 0
arr = [1,2,3,4,77,9]
for i in range(0, len(arr)):
  if c > arr[i]:
    print(c)
  else :
    c = arr[i]

print("Largest element in {} is {}".format(arr ,c) )


# In[3]:


#3.	Write a Python Program for array rotation?
arr = [1,2,3,4,77,9]
rot = []
l = len(arr) -1
for i in range(l , 0, -1):
  print(arr[i])


# In[4]:


#4.	Write a Python Program to Split the array and add the first part to the end?
l = int(input("Enter the lenth of arr : "))
arr = []

for i in range(l):
    arr.append(int(input()))
print("Arr is ",arr)
rotation = input("Enter Rotation Right/Left : ")
noro = int(input("Enter the number of elements to rotate  : "))
if noro > l:
    print("can not rotate as elements to rotate is larger then arr length")
else:
    rarr = []
    if rotation.upper() == "RIGHT":
        rarr[:] = arr[-noro:] + arr[:(l-noro)]
        print("After right rotation : ",rarr)
    elif rotation.upper() == "LEFT":
        rarr[:] = arr[noro:l] + arr[:noro] 
        print("After Left rotation : ",rarr)
    else:
        print("Wrong Entry")


# In[5]:


#5.	Write a Python Program to check if given array is Monotonic?
l = int(input("Enter the lenth of your list : "))
arr = []

for i in range(l):
    arr.append(int(input()))
print("The List  ",arr)

noro = int(input("Enter the number of elements to split  : "))
if noro > l:
    print("can not split as elements to split is larger then list lengh")
else:
    print("The split list is :",arr[:noro])
    rarr[:] = arr[noro:l] + arr[:noro]
    print("The List after split and add :", rarr)


# In[ ]:




