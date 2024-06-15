# You are working with a dataset of students and their course enrollments. Each student is
# represented by a unique student ID, and their course enrollments are stored in sets. (10 marks)
# [CO3][BTL3]
# i. Initialize sets for the course enrollments of three students: (2 marks)
# • Student 1 (ID: 101) is enrolled in courses A, B, and C.
# • Student 2 (ID: 102) is enrolled in courses B, C, and D.
# • Student 3 (ID: 103) is enrolled in courses C, D, and E.
# ii. Write a function called find_common_courses that takes two sets of course enrollments
# and returns a set containing the common courses. (2 marks)
# iii. Write a function called find_unique_courses that takes two sets of course enrollments
# and returns a set containing the courses that are unique to each student. (3 marks)
# iv. Write a function called find_all_courses that takes all three sets of course enrollments
# and returns a set containing all unique courses across all students. 


def find_common_courses(a,b):
    print(a[-1].intersection(b[-1]))

def find_unique_courses(a,b):
    print(a[-1].symmetric_difference(b[-1]))

def find_all_courses(a,b,c):
    u1=a[-1].union(b[-1])
    u2=a[-1].union(c[-1])
    uni=u1.symmetric_difference(u2)
    print(uni)

# Main Block

st1=[101,{'A','B','C'}]
st2=[102,{'B','C','D'}]
st3=[103,{'C','D','E'}]

# a=input("Enter the student1:")
# b=input("Enter the student2:")

find_common_courses(st1,st2)

find_unique_courses(st1,st2)
    
find_all_courses(st1,st2,st3)
