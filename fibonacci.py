#To print the fibonacci series till the user specified number

n=int(input("Enter the number:"))
if (n<=0):
    print("enter a valid number")
elif (n==1):
    print(1,end=' ')
else:
    a=0
    print(a,end=' ')
    b=1
    for i in range(1,n):
        print(b,end=' ')
        s=a+b
        a=b
        b=s
    