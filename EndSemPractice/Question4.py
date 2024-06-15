'''You've discovered a mystical text file named "magic_numbers.txt" that contains ten magical
6-digit numbers. Legend has it that these numbers possess a unique power, and their true
strength lies in their recursive sums.
Your task is to create a Python program that reads the numbers from the file, calculates their
sum using a recursive function, and then computes another recursive sum where each digit is
raised to the power of its position in the resultant sum.
Here's the step-by-step guide for your program:
1. Create a text file named "magic_numbers.txt" with the following content:
123456 234567 345678 456789 567890 678901 789012 890123 901234 123789
2. Write a Python program to read the numbers from the file and compute the recursive
sum. Use the compute_recursive_sum() function to calculate the sum of the magical
numbers. (2 + 3.5)
3. Write another recursive function compute_power_sum() that computes a recursive sum
of all digits in the sum computed in step 2 where each digit is raised to the power of its
position. (3.5)
For e.g., 5111439 is the recursive sum of all ten numbers listed in step 1. Then, the
power sum is 56 + 15 + 14 + 13 + 42 + 32 + 10
.
4. Your program should print the intermediate results i.e., recursive sum and the final
result i.e., power sum'''

def add(L):
    if len(L)<1:
        return 0
    else:
        return L[0] + add(L[1::])
    
def power():
    a=add(L)
    b=str(a)
    count=0
    for i in range(len(b)):
        count+= int(b[i]) ** (len(b)-i)
    return count
    


L=list(map(int,input("Enter the numbers:").split()))

print(add(L))

print(power())

