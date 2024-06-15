N=int(input())
l=[]
for i in range(N):
    num=int(input())
    l.append(num)
    
l=set(l)
    
n=int(input())
if n==1:
    a=int(input())
    if a in l:
        for i in range(1,a+1):
            if a%i==0:
                print(i,end=" ")
    else:
        print('Error')
        
elif n==2:
    k=[]
    M=max(l)
    for i in l:
        for j in range(1,M+1):
            if i%j==0:
                k.append(j)
    for i in k:
        if k.count(i)==1:
            print(i,end=' ')
            
else:
    print("Error")