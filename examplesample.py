
'''def main():

    def func():
        yield 1
        yield 2
        
    
    for i in func():
        print(i)

if __name__=='__main__':
    main()'''


# class person:

#     cl=12            # Class variable (changing this affects all the objects)

#     def __init__(self,name,age):
#         self.name=name
#         self.age=age              # Instance variable(changing this variable will not affect all objects,as it is unique 
#         person.details(self)      # for each objects)
                

#     def details(self):
#         print('name of the person:',self.name)
#         print('age of the person:',self.age)
#         print('class of the person:',self.cl)


# a=person('ak',21)
# a.details()
# b=person('ab',10)

# if a.age == b.age:
#     print('something')
# else:
#     print('skips')

# person.cl=10

# a.details()
# b.details()

# print(a,b)

        
class calculator:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,other):
        s1=self.a+self.b
        s2=other.a+other.b
        s3=calculator(s1,s2)
        return s3
    
    def __sub__(self,other):
        s1=self.a - self.b
        s2=other.a - other.b
        s3=calculator(s1,s2)
        return s3
    
    def __str__(self) -> str:
        return self.a,self.b
    
c1=calculator(5,2)
c2=calculator(20,5)
c3=c1 + c2
print(c3.a,c3.b)

var=9
print(var.__str__())    #Does the same printing operation
print(c3.__str__())



