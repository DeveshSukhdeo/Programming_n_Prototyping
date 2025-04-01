# Devesh Sukhdeo
# Period 1-2
# 4/1/25
# Python Coding Challenge #14
import turtle
import math

def draw_spiral(t, n, length, a, b):
    theta = 0.0
    for _ in range(n):
        t.forward(length)
        dtheta = 1 / (a + b * theta)
        t.left(math.degrees(dtheta)) 
        theta += dtheta

pepito = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("red")
draw_spiral(pepito, 1000, 5, 1, 1)
screen.mainloop()
