# 9/30/24
# Period 1-2
# Devesh Sukhdeo

# little Canadian kid broke their piggy bank
# you are to create a program to help them figure out how much money they have 
# pennies = 1 cent
# nickel = 5 cents 
# dimes = 10 cents 
# quarters = 25 cents 
# loonies = $1 or 100 cents 
# toonies = $2 or 200 cents
# ask the kid how many coins they have of each kind 
# calculate the total and give the answer in decimals and in a combination 
# i.e: $13.67 or $13 and 2 quarters, 1 dime, 1 nickle, 2 cent. 






#Other way
'''
pennies = int(input("How many pennies do you have? "))
nickles = int(input("How many nickels do you have? "))
dimes = int(input("How many dimes do you have? "))
quarters = int(input("How many quarters do you have? "))
loonies = int(input("How many loonies do you have? "))
toonies = int(input("How many toonies do you have? "))

# to find the total value of the coins, I multiplied the amount of coins by their individual value
p = pennies * 0.01
n = nickles * 0.05 
d = dimes * 0.10
q = quarters * 0.25
l = loonies * 1
t = toonies * 2 
totaldeci = p + n + d + q + l + t

print ("Your coins: " + str(toonies) + " toonies, " + str(loonies) + " loonies, " + str(quarters) + " quarters, " + str(dimes) + " dimes, " + str(nickles) + " nickles, " + str(pennies) + " pennies.")
print ("This adds up to: $" + str(totaldeci)) 
'''

