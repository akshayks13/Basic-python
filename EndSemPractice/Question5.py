'''You've stumbled upon a mysterious text file named "descending_numbers.txt" that contains
ten mystical numbers arranged in descending order. Legend has it that these numbers hold the
key to unraveling a hidden message. Your mission is to create a Python program that reads
these numbers, reverses them using a recursive function, and then performs a binary search on
the reversed list.
Here's the step-by-step guide for your program:
1. Create a text file named "descending_numbers.txt" with the following content:
98 87 76 65 54 43 32 21 10 5
2. Write a Python program to read the numbers from the file and store them in a list. (2)
3. Implement a recursive function reverse_list_recursive() that takes a list as input and
reverses it. Use the reverse_list_recursive() function to reverse the list of numbers
obtained in step 2. (3.5)
4. Implement another recursive function binary_search_recursive() that takes a sorted list
and a key to be searched as input and returns True if the key is found, and False
otherwise. Use the binary_search_recursive() function to perform a binary search on
the reversed list obtained in step 3. Choose a key from the list and print whether it was
found or not. (3.5)
5. Your program should display the original list, the reversed list, and the result of the
binary search.'''

# def rev(L,st,en):
#     if st < en:
#         L[st],L[en]=L[en],L[st]
#         rev(L,st+1,en-1)

def rev(L,st,en):
    while st < en:
        L[st],L[en] = L[en],L[st]
        st,en = st+1,en-1

L=[98,87,76,65,54,43,32,21,10,5]

rev(L,0,len(L)-1)
print(L)