# Devesh Sukhdeo
# Period 1-2
# 3/21/25
# Python Coding Challenge #11
import turtle
import math

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

#add squareL with length as parameter    
def squareL(t, length):
  for i in range(4):
    fd(t, length)
    lt(t, 90)

#added polygon with n parameter
def polygon(t, length, n):
  for i in range(n):
    fd(t, length)
    lt(t, (360/n))
    
#added circle with t and r as parameters
def circle(t, r):
  circ = 2 * math.pi * r
  n = 100
  length = circ / n
  polygon(t, length, n)

# added arc with t, r and angle as parameters   
def arc(t, r, angle):
  circ = 2 * math.pi * r 
  arcLength = (angle / 360) * circ  
  n = 100
  sideLength = arcLength / n 
  sideAngle = angle / n
  for i in range(n):
    fd(t, sideLength)
    lt(t, sideAngle)
    
screen = turtle.Screen()    
t = turtle.Turtle() 
t.speed(0)

draw(t, 10, 5)
bob = turtle.Turtle()

square(bob)
#call squareL function, useing 50 as side length
squareL(bob, 50)
#call polygon function
polygon(bob, 75, 6)
#call circle function 
circle(bob, 100)
#call arc function
arc(bob, 60, 180)

screen.mainloop()
