#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1.	Write a Python Program to Display Fibonacci Sequence Using Recursion?
def recurfib(n):
    if n<=1:
        return n
    else:
        return recurfib(n-1) + recurfib(n-2)

num = int(input("input no : "))

if num <=0:
    print("Please provide positive no.")

else:
    for i in range(num):
        print(recurfib(i) , end=" ")
       
    


# In[1]:


#2.	Write a Python Program to Find Factorial of Number Using Recursion?
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

num = int(input("input a no : "))

if num<0:
    print("Enter positive no.")
else:
    
        print(fact(num))


# In[2]:


#3.	Write a Python Program to calculate your Body Mass Index?
# BMI = weight / Height * height

h = float(input("enter your height in feet : "))
w = float(input("enter your weight in kilo : "))

bmi = w/(h**2)

print("The BIM is = ",bmi)


# In[3]:


#4.	Write a Python Program to calculate the natural logarithm of any number?
import math
x = int(input(("Enter a number : ")))
log = math.log(x)
print("Log of {} is {}".format(x, log))


# In[4]:


#5.	Write a Python Program for cube sum of first n natural numbers?
num = int(input("Enter a no :"))
sum = 0
for i in range(1 , num+1):
    sum = sum + i**3
print("Cube sum of {} natural numbers is {}".format(num,sum))    


# In[ ]:




