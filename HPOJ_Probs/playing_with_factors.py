N=int(input())
L=[]
for i in range(N):
    num=int(input())
    L.append(num)
    
    
m=max(L)
L=set(L)


n=int(input())
if n==1:
    l=[]
    d={}
    for i in L:
        for j in L:
            if i==j:
                pass
            elif i%j==0:
                l.append(j)

    if len(l)==0:
        print('Null')
    else:
        l=set(l)
        for i in l:
            print(i,end=' ')

            
elif n==2:
    l=[]
    d={}
    for i in L:
        for j in range(2,m+1):
            if i%j==0:
                l.append(j)
    if len(l)==0:
        print('Null')
    else:
        for i in l:
            d[i]=l.count(i) 
        ma=max(d.values())
        #print(d)           
        for i in d:
            if d[i]==ma:
                print(i,end=' ')

    
else:
    print("Error")
        

#OR


'''N = int(input())
numbers = []
factors = []
for i in range (1,N+1):
    val = int(input())
    numbers.append(val)
choice = int(input())

if choice == 1:
    for x in numbers:
        for y in numbers:
            if x==y:
                pass
            else:
                if x%y == 0:
                    factors.append(y)
    factor_set = set(factors)
    if len(factor_set) !=0:
        for x in factor_set:
            print(x,end=' ')
    else:
        print("Null")

elif choice == 2:
    for x in numbers:
        for i in range (2,x+1):
            if x%i == 0:
                factors.append(i)
    #print(factors)
    count1=0
    max1=set()
    for x in factors:
        if factors.count(x)>=count1 and factors.count(x)!=1:
            count1=factors.count(x)
            max1.add(x)
    if len(max1)!=0:
        for x in max1:
            if factors.count(x)>1:
                print(x,end=' ')
    else:
        print("Null")
else:
    print("Error")'''


    
    


