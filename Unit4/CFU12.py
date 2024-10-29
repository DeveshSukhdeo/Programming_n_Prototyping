#10/29/24
#Devesh Sukhdeo
#Period 1-2
'''
Write a program that asks the user for the password.
-The Password should initially be set to “simonsnyc”
-It keeps asking them for the password until they get it correct.
-For the incorrect password, it should say “Wrong Password!)
-For correct password it should say “Correct! You may enter….”
-And then it ends the program
'''
#CFU 12

password = "simonsnyc"
pword = input("What is the password")

while pword != password:
    print ("Wrong Password!")
    pword = input("What is the password")
print ("Correct, you may enter...")

    
