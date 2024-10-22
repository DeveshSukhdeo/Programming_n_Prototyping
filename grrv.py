import random
num_random1 = random.randint(1,10) 
num_random2 = random.randint(1,50)
num_random3 = random.randint(1,1000)
num_attempts = 0 

repeat = int(input("How many times you want to play (Up to five times)"))
difficulty = int(input("Choose difficulty 1, 2 or 3"))
total_attempts = 0

def dif(num_random1, num_attempts, repeat, difficulty):
    if diffliclty == 1:
        guess1(num_random1, num_attempts, repeat)
    elif difficulty == 2:
        guess2(num_random, num_attempts, repeat)
    else: 
        guess3(num_random, num_attempts, repeat)

def guess1(num_random1, num_attempts, repeat):
    guess_num = int(input("Guess the random number (1-10)")) 
    num_attempts = num_attempts + 1
    if guess_num == num_random1: 
        print("Your guess is correct, you made " + str(num_attempts) + " attempts.")
    elif guess_num > num_random1:
        print("Your guess is too high.")
        guess(num_random, num_attempts, repeat) 
    else: 
        print("Your guess is too low.")
        guess(num_random, num_attempts,repeat)
    total_attempts = total attempts + num_attempts
        
def guess2(num_random, num_attempts, repeat):
    guess_num = int(input("Guess the random number (1-10)")) 
    num_attempts = num_attempts + 1
    if guess_num == num_random: 
        print("Your guess is correct, you made " + str(num_attempts) + " attempts.")
    elif guess_num > num_random:
        print("Your guess is too high.")
        guess(num_random, num_attempts, repeat) 
    else: 
        print("Your guess is too low.")
        guess(num_random, num_attempts,repeat)
    total_attempts = total attempts + num_attempts
        
def guess3(num_random, num_attempts, repeat):
    guess_num = int(input("Guess the random number (1-10)")) 
    num_attempts = num_attempts + 1
    if guess_num == num_random: 
        print("Your guess is correct, you made " + str(num_attempts) + " attempts.")
    elif guess_num > num_random:
        print("Your guess is too high.")
        guess(num_random, num_attempts, repeat) 
    else: 
        print("Your guess is too low.")
        guess(num_random, num_attempts,repeat)
    total_attempts = total attempts + num_attempts


def num_repeat(repeat):
    if repeat == 1:
        guess(num_random, num_attempts, repeat)
    elif repeat == 2:
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
    elif repeat == 3:
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
    elif repeat == 4: 
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)        
    else:
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        guess(num_random, num_attempts, repeat)
        
average = total_attempts / repeat
        
guess(num_random, num_attempts,repeat)
num_repeat(repeat) 
print ("Your average score is: " + average)
dif(num_random1, num_attempts, repeat, difficulty)
