# Devesh Sukhdeo 
# Period 1-1
# 3/6/25
# Python Coding Challenge 3 

def four(a):
    a()
    a()
    a()
    a()
    
def make_grid():
    print ("+----+----+----+----+")
    print ("|    |    |    |    |")
    print ("|    |    |    |    |")
    print ("|    |    |    |    |")
    print ("|    |    |    |    |")
    print ("+----+----+----+----+")
    
four(make_grid)




# ------------
# Answer
# ------------

def print_beam():
    print("+----", end=" ") 
def print_post():
    print("|    ", end=" ")
def do_twice(f):
    f()
    f()
def print_beams():
    do_twice(print_beam)
    print("+")
def print_posts():
    do_twice(print_post)
    print("|")
def do_four(f):
    do_twice(f)
    do_twice(f)
def row():
    print_beams()
    do_four(print_posts)
def print_grid():
    do_twice(row)
    print_beams()
    
print_grid()
print (" ") 
def print_grid_twice():
    do_four(row)
    print_beams()

print_grid_twice()    
