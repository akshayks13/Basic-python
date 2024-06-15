L=[]
T=int(input())
for i in range(T):
    char_name,house,allies,enemies=map(str,input().split(','))
    L.append([char_name,house,allies,enemies])

n1=input()
n2=input()

d1={}
for i in L:
    print(i)