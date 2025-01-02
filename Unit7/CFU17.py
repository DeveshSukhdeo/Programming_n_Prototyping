# Devesh Sukhde0
# Period 1 - 2
# CFU #17
# Review + build in formatting functions 

box = "LoliPop"

def formatting(box):
    userInput = int(input("Choice?(1,2,3,4,5,6)"))
    if userInput == 1: 
        #Capitlaize the first letter of the variable
        box = box.capitalize()
        print(box)
    elif userInput == 2: 
        #Find and return the position of a value in the string
        box = box.find("i")
        print(box) 
    elif userInput == 3: 
        #Return true if the variable is a number
        box = box.isdigit()
        print(box)
    elif userInput == 4: 
        #Output the variable all lowercase
        box = box.lower()
        print(box)
    elif userInput == 5: 
        #Replace an index value item for another 
        print(box.replace("o", "a"))
    elif userInput == 6: 
        #Output all uppercase
        box = box.upper()
        print(box)
    else: 
        print("Not a valid option")

formatting(box)
