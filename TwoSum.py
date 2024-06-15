L=list(map(int,input("Enter a list of numbers :").split()))
target = int(input("Enter the number :"))

for i in L:
    for j in L[L.index(i) + 1::]:
        if i + j == target:
           print(L.index(i),L.index(j))
           print(i,j)
            