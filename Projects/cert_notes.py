import math

print("Item\tPrice\nApple\t1.75\nOrange\t3.50\nBanana\t2.25\nTotal\t9.00")

print("\n------------------\n")

minute = 60
print(2*(3-1))
print((1+1)**(5-2))
print((minute * 100)/60)
print(2**1+1)
print(3*1**3)
print(2*3-1)
print(6+4/2)

print("\n------------------\n")

first = 'throat'
second = 'warbler'
print(first + second)
print(first, second)
print(first +" "+ second)

print("\n------------------\n")

width = 17
height = 12.0
delimiter = "." 

print(width //2)
print(width / 2.0)
print(height / 3)
print(1 + 2 * 5)
print(str(delimiter) * 5)


# Part 2
print("\n------------------")
print("Part 2")
print("------------------\n")

print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

print("\n------------------\n")

x = 12
n = 20

print(bool(x > 0 and x < 10))
print(bool(n %2 == 0 or n %3 == 0))
print(bool(not(x>y)))

print("\n------------------\n")

r = 5
print ((4/3)*math.pi*r**3)

print("\n------------------\n")

cover_price = 24.95
discount = .40 
shipping_cost = 3
additional_copy_ship = .75 
num_copies = 60

price = cover_price * (1 - discount)  
total_cost = price * num_copies 
total_shipping = shipping_cost + additional_copy_ship * (num_copies - 1)
total_cost = total_cost + total_shipping 
print ("The total wholesale cost is $" + str(total_cost))

print("\n------------------\n")
