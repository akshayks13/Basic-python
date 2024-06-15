num=1
l=[]
while num==1:
    n=int(input())
    if n==10:
        print("Exiting Loop")
        print("Task Sheet Deleted")
        num=0
        
    else:
        if n==1:
            a=input()
            print("Added")
            l.append(a)
            print(l)
        if n==2:
            a=int(input())
            b=input()
            print("Added")
            l.insert(a,b)
            print(l)
        if n==3:
            a=input()
            print("Removed")
            l.remove(a)
            print(l)
        if n==4:
            a=int(input())
            print("Poped")
            l.pop(a)
            print(l)
        if n==5:
            print("Poped")
            l.pop()
            print(l)
        if n==6:
            l.sort()
            print("Sorted")
            print(l)
        if n==7:
            l.reverse()
            print("Reversed")
            print(l)
        if n==8:
            a=input()
            b=l.count(a)
            print("Count of " ,a," is",b)
        if n==9:
            print("Cleared")
            l.clear()
            print(l)

