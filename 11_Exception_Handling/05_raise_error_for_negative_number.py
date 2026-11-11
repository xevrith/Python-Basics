# Positive Number

number = int(input("Enter a positive number : "))

if number < 0:
    raise ValueError("Enter a positive number")
else:
    print(number)