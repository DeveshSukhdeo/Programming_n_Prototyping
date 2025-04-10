# Devesh Sukhdeo
# 4/9/2025
# Period 1-2
# Python Coding Challenge 20

def avoids(word, forbidden):
    for letter in word:
        if letter in forbidden: 
            return False 
    return True 

forbidden_input = input("Enter forbidden letters: ")
words = ["apple", "watermelon", "mango", "soda", "grapes","candy", "coffee"]
count = 0

for word in words: 
    if avoids(word, forbidden_input):
        count += 1 
        
print("Number of words that do not contain any forbidden letters:", count)

