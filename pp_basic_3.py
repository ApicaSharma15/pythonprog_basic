#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python Program to Check if a Number is Positive, Negative or Zero?
x = int(input("Enter a no."))
if x > 0 :
    print("{}  is a positive no.".format(x))
elif x < 0:
    print("{}  is a Negative no.".format(x))
else :
    print("it is zero")


# In[2]:


#2.	Write a Python Program to Check if a Number is Odd or Even?
x = int(input("Enter a no."))
if x%2 ==0:
     print("{}  is a even no.".format(x))
else:
     print("{}  is a odd no.".format(x))
    


# In[3]:


#3.	Write a Python Program to Check Leap Year?
x = int(input("Enter Year."))
if x%4 == 0:
    print("{}  is a Leap Year".format(x))
else:
    print("{}  is not a Leap Year".format(x))


# In[4]:


#4.	Write a Python Program to Check Prime Number?

x = int(input("Enter a no."))
for i in range(2,x):
    if x % i == 0:
        print("{} is not a prime no.".format(x))
        break
else:
              print("{} is  a prime no.".format(x))


# In[5]:


#5.	Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
x = int(input("Enter a number1: ")) 
y = int(input("Enter a number2: ")) 
for num in range(x,y):  
    if num > 1:
        for i in range(2,num):
            if (num%i) == 0:
                print(num,'is not a prime')                
                break
        else:
            print(num,'is a prime number')


# In[ ]:




