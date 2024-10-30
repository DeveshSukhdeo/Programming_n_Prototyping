#10/29/24
#Devesh Sukhdeo
#Period 1-2
'''
Version 1:
Write a program that asks the user for the password.
-The Password should initially be set to “simonsnyc”
-It keeps asking them for the password until they get it correct.
-For the incorrect password, it should say “Wrong Password!)
-For correct password it should say “Correct! You may enter….”
-And then it ends the program
Version 2: 
Modify Version 1 so that the User gets only 3 chances.
'''
#CFU #12

version = int(input("What version do you want to run? "))

def ver1(version):
    password = "simonsnyc"
    pword = input("What is the password")
    while pword != password:
        print ("Wrong Password!")
        pword = input("What is the password")
    print ("Correct, you may enter...")


def ver2(version):
    password = "simonsnyc"
    pword = input("What is the password")
    count = 0

    while pword != password and count < 2:
        print ("Wrong Password!")
        pword = input("What is the password")
        count = count + 1
    if pword == password:
        print ("Correct, you may enter...")
    else: 
        print ("Wrong Password!")

if version == 1:
    ver1(1)
else:
    ver2(1)
