#10/21/24
#Devesh Sukhdeo
#Period 1-2
#CFU #10 
#User needs to guess the random number. 

import random
num_random = random.randint(1,10) 
num_attempts = 0 

def guess(num_random, num_attempts):
    guess_num = int(input("Guess the random number (1-10)")) 
    num_attempts = num_attempts + 1
    if guess_num == num_random: 
        print("Your guess is correct, you made " + str(num_attempts) + " attempts.")
    elif guess_num > num_random:
        print("Your guess is too high.")
        guess(num_random, num_attempts)
    elif guess_num < num_random: 
        print("Your guess is too low.")
        guess(num_random, num_attempts)
    else: 
        return guess
    
guess(num_random, num_attempts)
