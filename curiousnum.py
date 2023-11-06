#Curious number is a number 
#Eg:145(1!+4!+5!=145)

import math

num=int(input("Enter the number:"))
a=num//100
num1=num%100
b=num1//10
c=num1%10

if ((math.factorial(a))+(math.factorial(b))+(math.factorial(c))==num):
    print(num,"is curious number")
else:
    print(num,"is not a curious number")
