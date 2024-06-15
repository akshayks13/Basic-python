# NumPy functions can accept arrays as arguments, allowing for efficient operations without loops.

from numpy import *

def func(arr):
    return arr**2

a=vectorize(func)
arr=array([1,2,3,4,5])
print(a(arr))