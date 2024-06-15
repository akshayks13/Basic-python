from numpy import*
a=array([[1,2,3],[4,5,6],[1,5,9]],dtype='float')
a_inv=linalg.inv(a)               # The `linalg.inv` function computes the inverse of a square matrix.
print(a_inv)
print(dot(a,a_inv))
