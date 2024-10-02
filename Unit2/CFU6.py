import random 
import math 

print ("Welcome to the random number generator! \nI will generate a number between 1 and 100.\n")

r_num = random.randint(1,100)
num1 = int(input("Enter a number: "))
print ("Results: ")
print ("Random Number Generated: " + str(r_num))           
print ("Entered Number: " + str(num1))

add = r_num + num1
subtract = r_num - num1
mult = r_num * num1 
quo = r_num / num1
rem = r_num % num1
sqr_root = math.sqrt(r_num)
power = num1**r_num 

print ("Sum: " + str(r_num) + " + " + str(num1) + " = " + str(add)) 
print ("Difference: " + str(r_num) + " - " + str(num1) + " = " + str(subtract))
print ("Product: " + str(r_num) + " * " + str(num1) + " = " + str(mult))
print ("Quotient: " + str(r_num) + " / " + str(num1) + " = " + str(quo))
print ("Remainder: " + str(r_num) + " % " + str(num1) + " = " + str(rem))
print ("Square Root of Random Number: " + "sqrt(" + str(r_num)+")" + " = " + str(sqr_root))
print ("Entered number to the power of Random Number: " + str(r_num) + " + " + str(num1) + " = " + str(power))
