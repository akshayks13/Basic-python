# Arrays can be saved to and read from files.

from numpy import *
a = arange(10)
a.tofile('myfile.dat')
b = fromfile('myfile.dat',dtype = 'int') 
print (b)

# The function fromfile() sets dtype=‘float' by default. In this case we have saved
# an integer array and need to specify that while reading the file. We could have saved 
# it as float the the statement a.tofile(‘myfile.dat', ‘float').