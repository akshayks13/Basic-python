#Program to find the factors of a number

n=int(input("Enter a number:"))
for i in range(2,n):
    if n%i==0:
        print(i)
        
