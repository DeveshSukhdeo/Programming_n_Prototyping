# Devesh Sukhdeo
# Period 1-2
# 2/27/25
# Python Coding Challenge 1

# Question 1
import math # import math so pi can be used
def sphere_volume(radius):  # creation of the function with radius as the parameter
    volume = (4/3) * math.pi * (radius ** 3)  # creation of variable storing the calculations for volume of a sphere
    return volume  #return to end tghe function

volume_result = sphere_volume(5)  # create variable to call function with parameter of 5
print(f"1. The volume of a sphere with a radius of 5 is {volume_result:.2f}")  # print the volume in a senetence using formatting 

# Question 2
def w_cost(copies):  # creation of function with copies as parameter
    cover_price = 24.95  # create variable to store cover price
    discount = 0.40  # create variable to store discount amount
    ship_first = 3  # create variable to store the ship first price 
    ship_after = 0.75  # create variable to store the ship after price
    discount_price = cover_price * (1 - discount)  # create variable to store calculations for the disount price
    total_book_cost = discount_price * copies  # create variable to store calculations for the total book cost, multiply discount price by amount of copies 
    shipping_cost = ship_first + (ship_after * (copies - 1))  # create variable to store calculatons for shipping cost, first book cost plus remaining book cost minus 1
    total = total_book_cost + shipping_cost  # create variable to store the total price, total book cost plus shipping cost
    print (f"2. Your total wholesale cost for 60 copies is ${total:.2f}")  # print the wholesale cost in a sentence using formatting
    
w_cost(60)  # call the function with 60 as parameter

# Question 3
def running_time(start_hour, start_minutes):  #  creation of a function with start hour and start minutes as parameters
    easy_pace = 8*60+15  # create variable to store calculations for the easy pace 
    tempo_pace = 7*60+12  # create variable to store calculations for the tempo pace
    total_time_seconds = easy_pace * 2 + (tempo_pace * 3)  # create variable to store the total time in seconds by adding the total easy pace miles and total tempo pace miles 
    total_minutes = total_time_seconds // 60  # create variable to store the total time in minutes, integral devision so there is no remainder
    total_seconds = total_time_seconds % 60  # create variable to store the total time in seconds, modulus so its just the remainder
    end_minutes = total_minutes + start_minutes  # create variable to store the total minutes, start minutes plus end minutes
    end_hour = start_hour  # create variable to store the start hour
    if end_minutes >= 60:  # if statement that takes effect if end minutes is less than or equal to 60
        end_hour += end_minutes // 60  # sets end_hour equal to end_minutes integral division 60
        end_minutes = end_minutes % 60  # sets end_minutes equal to end_minutes modulus 60 
    return end_hour, end_minutes  # return to end the function

end_hour, end_minutes = running_time(6, 52)  # calls the function in two variables with the parameters of 6 and 52 respectively
print (f"3. You will arrive home for breakfast at {end_hour}:{end_minutes} AM.") # prints the time in a sentence using formatting
    
