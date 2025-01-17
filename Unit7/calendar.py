def leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        return 1
    else: 
        return 0

def number_of_days(m, y):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 9, 11]:
        return 30
    elif m == 2:
        if leap_year(y):
            return 29 
        else:
            return 28
    else:
        return 0  

def days_passed(d, m, y):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(y):
        days_in_month[1] = 29 

    return sum(days_in_month[:m - 1]) + d - 1

def main():
    print("Please enter a date")
    day = int(input("Day: "))
    month = int(input("Month: "))
    year = int(input("Year: "))

    print("Menu:")
    print("1) Calculate the number of days in the given month.")
    print("2) Calculate the number of days passed in the given year.")
    choice = int(input())

    if choice == 1:
        days = number_of_days(month, year)
        print(days)
    elif choice == 2:
        passed_days = days_passed(day, month, year)
        print(passed_days)
    else:
        print("Invalid choice.")

main()

