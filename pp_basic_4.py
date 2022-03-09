#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1.	Write a Python Program to Find the Factorial of a Number?
x = int(input("Enter a Number "))
factorial = 1
if x < 0:
    print("Can not calculate Factorial of a negative number")
elif x == 0:
    print("Factorial of zero is 1")
else:
    for i in range(1,x+1):
        factorial = factorial * i
print("Factorial of {} is {}".format(x, factorial))


# In[2]:


#2.	Write a Python Program to Display the multiplication Table?
x = int(input("Enter a no for Table"))
print("Multiplication table for",x)
for i in range(1,11):
    print("{} x {} = {}".format(x , i , x*i))


# In[3]:


#3.	Write a Python Program to Print the Fibonacci sequence?
# Fibonacci series - > 1, 1, 2, 3, 5,8,13........
def genfib(n):
    a =1
    b= 1
    l =[]
    for i in range(n):
        l.append(a)
        a , b = b , a+b
    return l  


# In[4]:


genfib(6)


# In[5]:


#4.	Write a Python Program to Check Armstrong Number?
x = int(input("Enter the number : "))

power = len(str(x))

y = x
sum = 0
while y > 0:
    digit = y % 10
    sum = sum + digit ** power
    y = y//10
if x == sum :
    print("Number is armstrong number")
else:
    print("Not an armstrong number")


# In[6]:


#5.	Write a Python Program to Find Armstrong Number in an Interval?
## Find Armstrong Number in an Interval
x = int(input("Low no : "))
y = int(input("Up no : "))


for i in range(x,y+1):
    power = len(str(i))
    temp = i
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** power
        temp = temp//10
    if i == sum :
        print(i)


# In[8]:


#6.	Write a Python Program to Find the Sum of Natural Numbers?
x = int(input("enter the number : "))

sum = 0
for i in range(0,x+1):
    sum+=i
print("Sum of natural numbers upto {} is {}".format(x,sum))


# In[ ]:




