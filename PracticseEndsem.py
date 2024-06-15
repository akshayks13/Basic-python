'''s='Hi, I am Akshay of Cse-B'
print(s.split())'''

'''a=10
b='Akshay'
print(f'I am {b}, of class {a}')'''

'''a,b,c=map(int, input("Enter the Numbers : ").split(','))
print(a,b,c)'''

'''t=(1,2,3,4,5)
t=list(t)
t.remove(3)
t=tuple(t)
print(t)'''

'''d={1:'ak',2:'ab',3:'sa',4:'pr'}
x=d.items()
print(d)
print(x)'''

# s='''Beware the Jabberwock, my son,
# 	the jaws that bite, the claws that catch,
# 	Beware the JubJub bird and shun
# 	the frumious bandersnatch.'''

'''with open("carrol.txt",'w') as f:
    f.write(s)
    f.close()

with open("carrol.txt",'r') as f:
    a=f.readlines()
    print(a)
    longest=''
    for i in a:
        if len(i)> len(longest):
            longest = i
    print(longest)'''

# l=[1,2,3,4]
# t=list(l)
# a=l.copy()
# t[1]=100
# a[1]=100
# print('l:',l)
# print('t:',t)
# print('a:',a)


'''def length(L):
    highest=L[0]
    for i in L:
        if len(i)>len(highest):
            highest=i
    
    return highest

def rec_length(L,i=0,highest=''):
    if i==len(L):
        return highest
    
    curr=L[i]
    if len(highest) < len(curr):
        highest = curr
            
        
    return rec_length(L,i+1,highest)



# L=[]
# N=int(input("Enter the number of subjects:"))
# for i in range(N):
#     s=input("Enter the subjects:")
#     L.append(s)

L=['math','science','geography','politics']

print(rec_length(L))'''

'''a=[]
l=[(1,3), (7,7), (1,3), (7,8), (1,3), (7,7), (7,8), (4, 2), (7, 8), (7, 8), (4, 2), (4, 2)]
d={}
for i in l:
    d[i]=l.count(i)

for i in d.keys():
    a.append(i)

print(a)'''

'''def add(n):
    if n==0:
        return 0
    else:
        return n + add(n-1)

n=int(input("Enter the number:"))

print(add(n))'''

'''s1='akshay'
s2='abhinav'

for i,j in zip(s1,s2):
    print(i,j)
    if i==j:
        print('Same letter')
    else:
        pass'''

'''def find_line_pairs(points):
    horizontal_lines = {}
    vertical_lines = {}

    for point in points:
        x, y = point

        # Check for horizontal lines
        if y in horizontal_lines:
            horizontal_lines[y].append(point)
        else:
            horizontal_lines[y] = [point]

        # Check for vertical lines
        if x in vertical_lines:
            vertical_lines[x].append(point)
        else:
            vertical_lines[x] = [point]
    # print(horizontal_lines,vertical_lines) 
    return horizontal_lines, vertical_lines

def main():
    points = [(3, 4), (5, 10), (5, 4), (7, 10), (7, 3), (3, 2), (10, 4)]

    horizontal_lines, vertical_lines = find_line_pairs(points)

    for point in points:
        x, y = point

        # Print horizontal line pairs
        if y in horizontal_lines and len(horizontal_lines[y]) > 1:
            print(f"{point} - Horizontal line pairs: {horizontal_lines[y]}")

        # Print vertical line pairs
        if x in vertical_lines and len(vertical_lines[x]) > 1:
            print(f"{point} - Vertical line pairs: {vertical_lines[x]}")

if __name__ == "__main__":
    main()'''

'''for i in range(5):
    for j in range(1,i+1):
        print(j,end='')

    print('')'''



