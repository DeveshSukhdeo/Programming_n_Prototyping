#Devesh Sukhdeo 
#Period 1-2
#1/7/24
#CFU #18
'''
Write a program that adds up all of the prices in the list.
Hint: Use a for loop
'''

version = int(input("Which version do you want to run (1,2, or 3)?"))

#Version 1
def version1(version):
    prices = [1.95, 4.50, 0.99, 5.99]
    total = 0

    #Adds all the prices and prints the total
    for i in prices:
        total += i 
    print("The sum of the prices is: " + str(total))

#Version 2 
def version2(version):
    prices = []
    total = 0
    
    #Asks user for prices and adds them to the list
    amt = int(input("How many prices do you want to add?"))
    for i in range(amt):
        add_price = int(input("Enter a price: "))
        prices.append(add_price)
    
    #Finds and prints the total price
    for i in prices: 
        total += i
    print("The sum of the entered prices is" + str(total)) 
 
#Version 3
def version3(version):
    prices = []
    items = []
    total = 0
    
    #Ask use for items and adds them to the list
    amt_items = int(input("How many items do you want to add?"))
    for x in range(amt_items):
        item_names = input("Enter the names of the items you want to buy: ")
        items.append(item_names)
    
    #Asks user for prices and adds them to the list
    for i in range(amt_items):
        add_price = int(input("Enter the prices of the items you bought (In the same order): "))
        prices.append(add_price)
    
    #Prints the items along with their prices
    for y in range(len(items)):
        print("Item Name: " + str(items[y]) + "   -   Price: " + str(prices[y]))                   
    
    #Finds and prints the total price
    for i in prices: 
        total += i
    print("The total price of all items is: " + str(total))

#Asks user which version they want to run    
if version == 1:
    version1(version)
elif version == 2:
    version2(version) 
else: 
    version3(version) 
