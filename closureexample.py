
# What are Python Closures
# A Closure in Python is a function object that remembers values in enclosing scopes even if 
# they are not present in memory. 

# It is a record that stores a function together with an environment: a mapping associating each free variable 
# of the function (variables that are used locally but defined in an enclosing scope) with the value or reference 
# to which the name was bound when the closure was created.
# A closure—unlike a plain function—allows the function to access those captured variables through the 
# closure’s copies of their values or references, even when the function is invoked outside their scope.

def func(a,b):

    def inner():
        return a*b
    
    return inner

# calling a function with a variable

# print(func(2,3))
a=func(2,3)
print(a())






