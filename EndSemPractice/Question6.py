'''You've discovered an ancient text file named "number_power_product.txt" that holds the key
to unlocking mystical powers hidden within numbers. The file contains five pairs of numbers
written as a single sequence, where even positions represent bases or multiplicands, and odd
positions represent exponents or multipliers. Your mission is to create a Python program that
reads these pairs, performs computations using two recursive functions, and unveils the
magical results.
Here's the step-by-step guide for your program:
1. Create a text file named "number_power_product.txt" with the following content:
2 3 4 2 5 4 3 2 6 3
2. Write a Python program to read these numbers from the file and store them in a list. (2)
3. Implement a recursive function compute_power_recursive() that takes two arguments
(base and exponent) and computes the power of a number. Use the
compute_power_recursive() function to calculate the powers using the even positions
(0, 2, 4, ...) as bases and odd positions (1, 3, 5, ...) as exponents from the list obtained
in step 2. (3.5)
4. Implement another recursive function compute_product_recursive() that takes two
arguments (multiplicand and multiplier) and computes their product. Use the
compute_product_recursive() function to find the product of numbers using the even
positions (0, 2, 4, ...) as multiplicands and odd positions (1, 3, 5, ...) as multipliers from
the list obtained in step 2. (3.5)
5. Print the original list, the computed powers, and the computed products'''

'''def compute_power_recursive(L):
    for i in range(0,len(L)-1,2):
        L_power.append(L[i]**(L[i+1]))

def compute_product_recursive(L):
    for i in range(0,len(L)-1,2):
        L_product.append(L[i]*(L[i+1]))

L=[2,3,4,2,5,4,3,2,6,3]
L_power=[]
L_product=[]

compute_power_recursive(L)
compute_product_recursive(L)

print(L_power)
print(L_product)'''

# _________ OR ________ #


def compute_power_recursive(L, index=0):
    if index >= len(L):
        return []

    base = L[index]
    exponent = L[index + 1]
    result = [base ** exponent] + compute_power_recursive(L, index + 2)
    return result

def compute_product_recursive(L, index=0):
    if index >= len(L):
        return []

    multiplicand = L[index]
    multiplier = L[index + 1]
    result = [multiplicand * multiplier] + compute_product_recursive(L, index + 2)
    return result

L = [2, 3, 4, 2, 5, 4, 3, 2, 6, 3]

L_power = compute_power_recursive(L)
L_product = compute_product_recursive(L)

print("Computed Powers:", L_power)
print("Computed Products:", L_product)
