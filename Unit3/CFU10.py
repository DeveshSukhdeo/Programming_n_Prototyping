import random
num_random = random.randint(1,10) 
num_attempts = 0 

def guess(num_random, num_attempts):
    guess_num = int(input("Guess the random number (1-10)")) 
    num_attempts = num_attempts + 1
    if guess_num == num_random: 
        print("Your guess is correct, you made " + num_attempts + " attempts.")
    elif guess_num > num_random:
        print("Your guess is too high.")
        return guess
    elif guess_num < num_random: 
        print("Your guess is too low.")
        return guess
    else: 
        return guess
    
 
