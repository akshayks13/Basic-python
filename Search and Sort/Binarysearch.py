l=list(map(int,input("Enter the numbers:").split()))
l.sort()
print(l)
m=int(input("Enter the element to be searched:"))
low=0
high=len(l)-1
while low < high:
    mid=(low + high)//2
    if m > l[mid]:
        low=mid+1
    elif m < l[mid]:
        high=mid-1
    else:
        low=high
        print("Element found at position:",mid)
        
       
        
    
