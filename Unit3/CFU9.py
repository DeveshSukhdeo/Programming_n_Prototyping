#10/17/24
#Devesh Sukhdeo
#Period 1-2
#Guessing game roll of the dice 
#CFU9

import random
rolls = input("How many rolls do you want to play?")
g_num = input("Guess a number between 1 and 6: ")
r_num = random.randint(1,6)

print("Guessed number: " + str(g_num))
print("Random number: " + str(r_num))

if g_num == r_num:
    points = 0 
    points2 = points + 6
    print("Your total points are: " + str(points2))
elif g_num != r_num: 
    points = 0
    points2 = points - 1 
    print("Your total points are: " + str(points2))
else: 
    print("Your total points are: " + str(points))
 
    


