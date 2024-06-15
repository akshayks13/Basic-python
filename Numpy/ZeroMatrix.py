#  The `zeros` function creates arrays filled with zeros.
#  Syntax: zeros(shape, datatype)
#  zeros( [3,2], ‘float') generates a 3 x 2 array filled with zeros as shown below.
# 0.0 0.0 0.0
# 0.0 0.0 0.0
# If not specified, the type of elements defaults to int.

from numpy import*
a=zeros([3,3],'int')
b=zeros([3,3],'int')
print(a+b)
print(a*b)