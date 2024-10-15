#Devesh Sukhdeo
#Period 1-2 
#10/15/24
'''
GrubHub Program
Version 1: If the user responds “yes” - say great!
If the user responds with anything else say: “NO?! So who is cooking?”
'''

order = str(input("Did you order delivery?"))
if order == "yes" or order == "Yes" or order == "YES" or order == "Y" or order =="y":
    print("Great!")
    cost = float(input("What was the cost of your food? "))
    people = int(input("How many people are splitting the order? "))
    cpp = cost/people
    print ("The cost per person is $" + str(cpp))
else:
    print("NO?! So who is cooking?")
