# Devesh Sukhdeo
# Period 1-2
# 3/18/25
# Python Coding Challenge #9
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

def square(t, length):
  for i in range(4):
    fd(t, length)
    lt(t, 90)

#added polygon with n parameter
def polygon(t, length, n):
  for i in range(n):
    fd(t, length)
    lt(t, (360/n))
    
screen = turtle.Screen()    
t = turtle.Turtle() 
t.speed(0)

draw(t, 10, 5)
bob = turtle.Turtle()

square(bob, 150)
#call polygon function
polygon(bob, 50, 10)

screen.mainloop()
