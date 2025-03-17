# Devesh Sukhdeo
# Period 1-2
# 3/17/25
# Python Coding Challenge #8
import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length*n)
    t.left(angle)
    draw(t, length, n-1)
    t.right(2*angle)
    draw(t, length, n-1)
    t.left(angle)
    t.backward(length*n)

def fd(x, y):
  turtle.Turtle.forward(x, y)
def lt(x, y):
  turtle.Turtle.left(x, y)

#added length parameter
def square(t, length):
  for i in range(4):
    fd(t, length)
    lt(t, 90)
    
screen = turtle.Screen()    
t = turtle.Turtle() 
t.speed(0)

draw(t, 10, 5)
bob = turtle.Turtle()

#give value to length
length = 200
square(bob, length)

screen.mainloop() 
