# Devesh Sukhdeo
# Period 1-2
# 4/1/25
# Python Coding Challenge #13
import turtle

def polygon(t, length, n):
    for _ in range(n):
        t.forward(length)
        t.left(360 / n)

def draw_lines(t, length, n):
    for _ in range(n):
        t.forward(length)
        t.backward(length)
        t.left(360 / n)

def draw_shape(t, length, n, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    polygon(t, length, n)
    t.penup()
    t.goto((length/x+1), (length+y-6))
    t.pendown()
    draw_lines(t, length, n)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.speed(0)

draw_shape(bob, 50, 6, 2, 2) 
screen.mainloop()

