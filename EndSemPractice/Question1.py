# You are tasked with creating a program to manage employee data. Each employee's
# information is represented using a tuple, where the elements are (employee_id, name,
# position, salary). (10 marks) [CO3][BTL3]
# i. Create a list called employees to store the employee information. (2 marks)
# ii. Write a function called add_employee that takes parameters for employee information
# (id, name, position, salary) and adds a new tuple to the employees list. (3 marks)
# iii. Write a function called find_highest_paid that finds and prints the details of the
# employee with the highest salary. (3 marks)
# iv. Write a function called display_employees that prints out the details of each employee.

L=[]

def add_employee(id,name,position,salary):
    t=(id,name,position,salary)
    L.append(t)


def find_highest_paid(L):
    highest=0
    for i in L:
        if i[-1]>highest:
            highest=i[-1]
    for i in L:    
        if highest in i:
            print("The details of the highest earned employee is:",end=' ')
            print(i)
        
def display_employees(L):
    print("The datails of the employees are:")
    for i in L:
        print(i)


# Mainblock

n=int(input("Enter the number of employees to be added:"))
for i in range(n):
    id=int(input("Enter the id:"))
    name=input("Enter the name:")
    position=input("Enter the position:")
    salary=float(input("Enter the salary:"))
    add_employee(id,name,position,salary)

find_highest_paid(L)

display_employees(L)