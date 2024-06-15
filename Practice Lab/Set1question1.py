
'''def length(s):
    count=0
    for i in s:
        if i!='':
            count+=1

    return count'''


#---------------OR---------------#

def length(s):
    if s=='':
        return 0
    else:
        return 1 + length(s[1:])
    
   
def sub(arr):
    L=[]
    for i in Subjects:
        L.append(length(i))

    return L

N=int(input("Enter the number of Subjects:"))
Subjects=[]
for i in range(N):
    s=input("Enter the subjects:")
    Subjects.append(s)

print(sub(Subjects))
