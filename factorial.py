'''import math

num=int(input(""))
print(math.factorial(num))'''

#---------OR--------

num=int(input("Enter the number:"))
s=num
if num==0:
    print(1)
elif num==1:
    print(1)
else:
    for i in range(1,num):
        s=s*i

    print(s)








