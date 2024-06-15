#Run the code and find the number of steps untill the number is 1
#if number is even n/2
#if number is odd 3n+1

n=int(input("Enter the number:"))
s=0

while n!=1:
    if n%2==0:
        s=s+1
        n=n/2
        print(n,end="-->")
    else:
        s=s+1
        n=(3*n)+1
        print(n,end="-->")
else:
    s=s+1
    print("STOP")
    print("No. of steps=",s)


print("")













'''if n==1:
    s=s+1
    print("STOP")
    print("No. of steps=",s)'''