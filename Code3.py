def is_leap_year(year):
    # Leap year if it's divisible by 4
    if year % 4 == 0:
        # Except if it's divisible by 100 but not divisible by 400
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Taking input from the user
year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
