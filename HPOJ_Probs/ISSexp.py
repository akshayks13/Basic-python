L=[]
T=int(input())
for i in range(T):
    expname,research_field,countries,year=map(str,input().split(','))
    L.append([expname,research_field,countries,year])

country=input()
#print(L)

'''d1={}
a={}
research_list=[]
for i in L:
    res=i[1]
    research_list.append(res)
for i in L:
    for j in research_list:
        if j==i[1]:
            a
for i in research_list:
    d1[i]=research_list.count(i)

for i in d1:
    for j in L:
        if i==j[1]:
            a[i]=j[0]

for i in d1:
    for j in a:
        for k in L:
            if i==j:
                print(i,j[i],k[0])
               

exp_list=[]    
print("Experiments with",country,':',end=' ')
for i in L:
    #print('Experiments with USA:',end=' ')
    if country in i[2]:
        exp_list.append(i[0])

for i in exp_list:
    print(i,end=',')'''


d={}
r_list=[]
for i in L:
    re=i[1]
    r_list.append(re)
for i in r_list:
    d[i]=r_list.count(i)

for i in d:
    ma=max(d.values())
    if d[i]==ma:
        print('Most Collaborative Field:',i)



    
