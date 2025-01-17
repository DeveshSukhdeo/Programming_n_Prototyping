# Function to validate the month
def validateMonth(month):
    while month < 1 or month > 12:
        month = int(input("Invalid month. Please enter a value from 1-12: "))
    return month

# Function to validate the day
def validateDay(month, day, year):
    # Determine the number of days in the month
    if month in [4, 6, 9, 11]:  
        max_days = 30
    elif month == 2: 
        # Check for leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_days = 29
        else:
            max_days = 28
    else:  
        max_days = 31

    while day < 1 or day > max_days:
        day = int(input(f"Invalid day. Please enter a value from 1-{max_days}: "))
    return day

# Function to add an event
def addEvent():
    event_name = input("What is the event: ")
    year = int(input("What is the year: "))
    
    month = int(input("What is the month (number): "))
    month = validateMonth(month)
    
    day = int(input("What is the date: "))
    day = validateDay(month, day, year)
    
    
    eventName.append(event_name)
    eventYear.append(year)
    eventMonth.append(month)
    eventDay.append(day)

# Function to print events
def printEvents():
    print("\n******************** List of Events ********************")
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]
    for i in range(len(eventName)):
        print(eventName[i])
        print(f"Date: {month_names[eventMonth[i] - 1]} {eventDay[i]}, {eventYear[i]}")

# MAIN 
eventName = []  
eventMonth = []  
eventDay = []  
eventYear = []  

# Allow user to enter events
addEvent()
while input("Do you want to enter another event? NO to stop: ").strip().lower() != "no":
    addEvent()

printEvents()
