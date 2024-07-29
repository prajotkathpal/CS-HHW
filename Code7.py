def display_digits(number):

    number_str = str(number)
    
    for digit in number_str:
        print(digit)

number = int(input("Enter a number: "))


print("Digits of the number:")
display_digits(number)
