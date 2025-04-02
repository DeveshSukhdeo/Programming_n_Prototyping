# Devesh Sukhdeo
# Period 1-2
# 4/2/25
# Python Coding Challenge #15
import turtle

# Function to draw a Koch curve of a given length
def koch_curve(t, length):
    # The function checks if the length is smaller than 3, in which case it draws a straight line
    if length < 3:
        t.forward(length)
        return
    # Otherwise, it recursively breaks down the curve into smaller segments, turning the turtle accordingly
    length /= 3 
    # Recursively draw the first third of the curve
    koch_curve(t, length)
    # Turn the turtle left by 60 degrees
    t.left(60)
    # Recursively draw the second third of the curve
    koch_curve(t, length)
    # Turn the turtle right by 120 degrees
    t.right(120)
    # Recursively draw the third third of the curve
    koch_curve(t, length)
    # Turn the turtle left by 60 degrees
    t.left(60)
    # Recursively draw the final third of the curve
    koch_curve(t, length)

# Function to draw a snowflake by drawing three Koch curves
def snowflake(t, length):
    # Loop 3 times to draw 3 sides of the snowflake
    for _ in range(3):
        # Draw a single Koch curve with the specified length
        koch_curve(t, length)
        # Turn the turtle right by 120 degrees to form the snowflake shape
        t.right(120)

pepito = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("white")
pepito.speed(0)

pepito.penup()
pepito.goto(-150, 100)
pepito.pendown()

snowflake(pepito, 300)
screen.mainloop()
