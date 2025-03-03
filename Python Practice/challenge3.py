# Devesh Sukhdeo
# Period 1-2 
# 3/3/25
# Python Challenge #3

def do_twice(f, value):
    f(value)
    f(value)
    
def print_twice(value):
    print(value)
    print(value)

do_twice(print_twice, "spam") 

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)
    
do_four(print_twice, "spam") 





    
