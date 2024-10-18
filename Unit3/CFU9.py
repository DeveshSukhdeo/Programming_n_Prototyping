#10/17/24
#Devesh Sukhdeo
#Period 1-2
#Guessing game roll of the dice 
#CFU9

import random
print("Let's roll the dice!")

num_rolls = int(input("How many times do you want to roll the dice? "))

def guess(num_random, total):
    user_guess = int(input("Guess the roll: "))
    if user_guess == num_random:
        total = total + 6
    else:
        total = total - 1 

def rolls(num_rolls, total = 0):
    num_random = random.randint(1,6)
    if num_rolls == 0:
        return total
    else: 
        num_rolls = num_rolls - 1        
        guess(num_random, total)
        print (f"You rolled a {num_random}!")
        return rolls(num_rolls, total)
    
total = rolls(num_rolls)
print(f"The total is: {total}") 
