ans=input()
n=int(input())
l=[]
for i in range(n):
    stu=input()
    s=0
    for i in range(10):
            if ans[i]==stu[i]:
                s+=1
    l.append(s)
print(l)