# 1. Create a 1D array with elements 5, 10, 15, 20, 25. Slice the first three elements.

'''from numpy import*
a=arange(5,25,5)
arr=array(a)
print(arr[:3])'''


#2.Create a 3x2 matrix and sum its elements using loops.

'''from numpy import*

a=random.random([3,2])
print(a)
count=0
for i in a:
    for j in i:
        count+=j
print(count)'''


# Use linspace to create an array from 0 to 10 with a stepsize of 0.1.
# Use arange to create a 100-element array from 0 to 10.

'''from numpy import*

a=linspace(0,10,101)  #linspace cannot have step value it can only have the number of terms between the two numbers
print(a)
b=arange(0,10,0.1)    #arange uses the step value and prints those values between the two numbers
print(b)'''

# Copy array a = [2,3,4,5] to b, modify b, and print both.


'''from numpy import*

a = array([2, 3, 4, 5])

# Copy array a to b
b = copy(a)

# Modify array b
b[0] = 10

# Print both arrays
print("Array a:", a)
print("Array b:", b)'''


# Multiply a 3x3 matrix by 5.

'''from numpy import*

a=array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])
result=a*5

print(result)'''


# Add two 3x3 matrices.

'''from numpy import*

a = array([[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]])

b = array([[9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]])

print(a+b)'''

# Demonstrate dot and cross products.

'''from numpy import*

a=array([1,17,18])
b=array([10,11,7])

print(dot(a,b))    #The `dot` function computes the dot product of two vectors.
print(cross(a,b))   #The `cross` function computes the cross product of two vectors.'''


# Solve a system of equations using matrix inversion.

'''from numpy import*

# Coefficient matrix
a = array([[2, 1],
          [3, -2]])

# Right-hand side matrix
b = array([[5],
           [8]])

a_inv=linalg.inv(a)

x=print(a_inv * b)'''


# Find new coordinates of (10,10) after rotation by π/4.

'''from numpy import*

cord=array([10,10])
x=cord[0]
y=cord[1]
print(x,y)

ang=pi/4

new_cord=array([[x * cos(ang) - y * sin(ang)], [x * sin(ang) + y * cos(ang)]])

print(new_cord)'''


# Write a vectorized function for y = x2 and test with x=[1,2,3].

'''from numpy import*

def func(arr):
    return arr ** 2

a=array([1,2,3])
vec=vectorize(func)
print(func(vec(a)))'''








