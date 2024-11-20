# Dictionary mapping month numbers to the number of days
month_days = {
    1: 31,  # January
    2: 28,  # February (non-leap year default)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31   # December
}

# Ask the user for a month number
month = input("Enter the month number (1-12): ")

if month.isdigit():
    month = int(month)
    if 1 <= month <= 12:
        # Handle February for leap years
        if month == 2:
            leap_year = input("Is it a leap year? (yes/no): ").strip().lower()
            if leap_year in ["yes", "y"]:
                print("February has 29 days in a leap year.")
            elif leap_year in ["no", "n"]:
                print("February has 28 days.")
            else:
                print("Invalid input for leap year. Assuming non-leap year.")
                print("February has 28 days.")
        else:
            print(f"The month {month} has {month_days[month]} days.")
    else:
        print("Invalid month number. Please enter a number between 1 and 12.")
else:
    print("Invalid input. Please enter a numeric value.")
