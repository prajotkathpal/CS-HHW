def digit_to_word(digit):
    words = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    return words.get(digit)


number = input("Enter a 3-digit number: ")


if number.isdigit() and len(number) == 3:
   
    for digit in number:
        print(digit_to_word(digit))
else:
    print("Invalid input. Please enter a 3-digit number.")
