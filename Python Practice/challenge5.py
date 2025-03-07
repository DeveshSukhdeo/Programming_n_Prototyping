# Devesh Sukhdeo 
# Period 1-2
# 3/6/25
# Python Coding Challenge 5

def check_fermat(a, b, c, n):
    if n > 2 and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn’t work")
        
check_fermat(2, 2, 2, 4)
