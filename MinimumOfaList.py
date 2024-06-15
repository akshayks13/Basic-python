l=list(map(int,input("Enter the numbers:").split()))
mini=l[0]
for i in range(len(l)):
    if l[i]<mini:
        mini=l[i]

print(mini)

    