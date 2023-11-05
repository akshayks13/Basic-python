#To print the even and odd numbers in a given range
num1=int(input("Enter first number:"))
num2=int(input("Enter first number:"))

for i in range(num1,num2):
    if i%2==0:
        print(i,"is even")
    else:
        print(i,"is odd")
