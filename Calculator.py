#To create a calculatore using functions

#main
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))

print("CALCULATOR")
print("Enter 1 to add")
print("Enter 2 to subtract")
print("Enter 3 to multiply")
print("Enter 4 to divide")

choice=int(input("Enter the choice:"))


#Function blocks

def addd(x,y):
    print("The sum of",x,"and",y,"is",x+y)

def subt(x,y):
    print("The subtraction of",x,"and",y,"is",x-y)

def mult(x,y):
    print("The multiplication of",x,"and",y,"is",x*y)

def div(x,y):
    print("The division of",x,"and",y,"is",x/y)

   
#Function call
if choice==1:
    addd(num1,num2)

elif choice==2:
    subt(num1,num2)

elif choice==3:
    mult(num1,num2)

elif choice==4:
    div(num1,num2)

else:
    print("Enter any valid choice")

