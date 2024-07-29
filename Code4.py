def is_valid_date(day, month, year):
    
    if month < 1 or month > 12 or day < 1:
        return False


    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  
    if is_leap_year(year):
        days_in_month[1] = 29

    
    if day > days_in_month[month - 1]:
        return False

    return True

def is_leap_year(year):
   
    if year % 4 == 0:
        
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


date_input = input("Enter a date in the format (dd/mm/yyyy): ")


day, month, year = map(int, date_input.split('/'))


if is_valid_date(day, month, year):
    print("The date entered is valid.")
else:
    print("The date entered is not valid.")
