# Devesh Sukhdeo
# Period 1-2
# 3/14/25
# Python Coding Challenge #7
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
def square(t):
  for i in range(4):
    fd(t, 100)
    lt(t, 90)
    
screen = turtle.Screen()    
t = turtle.Turtle() 
t.speed(0)

draw(t, 10, 5)
bob = turtle.Turtle()
square(bob)

screen.mainloop() 
