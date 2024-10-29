#10/25/24
#Devesh Sukhdeo
#Period 1-2
'''
Create  function for each of these:
1) Using For Loop Create a program that prints out the numbers:  10, 20, 30, 40, 50 up to 70
2) Using For Loop create a program that prints out the numbers: 0, 0.5 , 1 , 1.5, 2 ….   up to 10.0
3) Sing the 99 bottles of beer song
Write a Program that gives you the option to run 1, 2 or 3 functions as per user request.
'''
#CFU #11

run = int(input("How many loops do you want to run? 1-3 "))

def count1(c):
    for c in range(10, 71, 10):
        print(c)
    print(" ")


def half_count(x): 
    for x in range(0, 21):
         print(x * 0.5)
    print(" ")

def beer(i):            
    for i in range(99, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down and pass it around, {i - 1} bottles of beer on the wall.\n")
        else:
            print(f"{i} bottle of beer on the wall, {i} bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")            
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")

if run == 1:
    count1(1)
elif run == 2:
    count1(1)
    half_count(1)
else:
    count1(1)
    half_count(1)
    beer(1) 
