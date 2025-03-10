# Devesh Sukhdeo
# Period 1-2
# 3/10/25
# Python Coding Challenge 6

def is_triangle(l1, l2, l3):
    if (l1 > l2 + l3) or (l2 > l3 + l1) or (l3 > l2 + l1):
        return "No"
    else: 
        return "Yes"
    
def input_lengths():
    length1 = int(input("Enter the length of side 1: "))
    length2 = int(input("Enter the length of side 2: "))
    length3 = int(input("Enter the length of side 3: "))
    print(is_triangle(length1, length2, length3)) 
          
input_lengths() 
