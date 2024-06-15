# You are tasked with creating a simple inventory management system for a small store. The
# store sells different types of products, and the inventory data is stored in a list of tuples. Each
# tuple represents a product and contains the following information: (product_id, product_name,
# quantity, price_per_unit) (10 marks) [CO3][BTL3]
# i. Initialize an empty list called inventory to store the product information. (2 marks)
# ii. Write a function called add_product that takes parameters for product information (id,
# name, quantity, price) and adds a new tuple to the inventory list. (2 marks)
# iii. Write a function called update_quantity that takes a product ID and a quantity to add or
# subtract. This function should update the quantity of the specified product in the
# inventory. (2 marks)
# iv. Write a function called calculate_inventory_value that calculates and returns the total
# value of the inventory (sum of quantity * price for each product). (2 marks)
# v. Write a function called display_inventory that prints out the details of each product in
# the inventory

def add_product(id,name,quantity,price):
    t=(id,name,quantity,price)
    L.append(t)

def update_quantity(id,quantity):
    num=int(input("Entet 1 to add quantity and 2 to subtract quantity:"))
    for i in range(len(L)):
        L[i]=list(L[i])
        if L[i][0]==id:
            if num == 1:
                L[i]=tuple([L[i][0],L[i][1] ,L[i][2]+quantity,L[i][3]])
            elif num == 2:
                L[i][2]-=quantity
        
        
def calculate_inventory_value(L):
    Total_cost=0
    for i in L:
        Total_cost+= i[-1] * i[-2]
    print(Total_cost)

def display_inventory(L):
    print("The products of the inventoary are:")
    for i in L:
        print(i)


# Main Block

L=[]
while True:
    choice=int(input("Enter choice to continue or exit:"))
    if choice == 1:
        n=int(input('Enter the choice:'))
        if n==1:
            id=int(input("Enter the id:"))
            name=input("Enter the name:")
            quantity=int(input("Enter the quantity:"))
            price=float(input("Enter the price:"))
            add_product(id,name,quantity,price)
        elif n==2:
            id=int(input("Enter the id:"))
            quantity=int(input("Enter the quantity:"))
            update_quantity(id,quantity)
        elif n==3:
            calculate_inventory_value(L)
        elif n==4:
            display_inventory(L)
    
    elif choice == 2:
        break




