l=list(map(int,input("Enter the numbers:")))
# print(l)
m=int(input("Enter the number to be searched:"))
for i in l:
    if i==m:
        print("Element is found at index:",l.index(i))
        break
    else:
        pass
