# def func(l,s):
#     count=0
#     for i in l:
#         if s in i:
#             count+=1

#     return count


#-------------OR------------#


def func(l,s):
    n=len(l)
    if n==1:
        if s in l[0]:
            return 1 
    for i in range(n):

        if s in l[i]:
            return 1 + func(l[1::],s)
        else:
            return 0 + func(l[1::],s)
       


        




N=int(input("Enter the number of neighbouring countries:"))
Neighbours=[]
for i in range(N):
    country=input("Enter the country:")
    Neighbours.append(country)

s=input("Enter the substring:")

print(func(Neighbours,s))
