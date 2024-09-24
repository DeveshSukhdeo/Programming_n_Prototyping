#9/24/24
#Period 1-2
#Devesh Sukhdeo
#Quadratic formula solve 

import math 
name = input("Enter your name: ")
print("Hello " + name + "!")
a = float(input("Enter the a coefficient: "))
b = float(input("Enter the b coefficient: "))
c = float(input("Enter the c coefficient: ")) 
print("Your quadratic equation is: " + str(a) + "x^2 + " + str(b) + "x + " + str(c)) 
x1 = (-b + math.sqrt(b**2 - (4*a*c))) / (2*a) 
x2 = (-b - math.sqrt(b**2 - (4*a*c))) / (2*a)
print("The roots of the equation are: x1 = " + str(x1) + " x2 = " + str(x2)) 

