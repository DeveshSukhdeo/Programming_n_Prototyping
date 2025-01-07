groceries = ["Eggs", "Apples", "Milk", "Bread"]
names = ["Vashti", "Wendy", "Towaf", "Syeda", "Jerelyn", "Jannatul", "Micah", "Armina", "Samuel", "Rohan", "David", "Nataly", "Aliyah", "Rafael", "Nabila", "Tasfia", "Brithany", "Michael", "Betsy"]
ages = [17.4, 16.0, 16.6, 16.5, 16.0, 16.2, 16.4, 16.11, 16.0, 16.6, 17.2, 16.11, 16.11, 17.2, 16.5, 16.2, 17.1, 16.3, 16.2]  

print(groceries[0]) 
print(names[0] + " is " + str(ages[0]) + " years old.") 
print(str(names[1:5]) + " is " + str(ages[1:5]) + " years old.")
print(" ") 

for i in range(len(names)): 
    print("My friend " + names[i] + " is " + str(ages[i]) + " years old.") 

print(" ")    
groceries.append("Cabbage")
print(groceries)

print(" ")    
groceries.insert(1, "Carrot")
print(groceries)

print(" ")    
groceries.remove("Eggs")
print(groceries)
