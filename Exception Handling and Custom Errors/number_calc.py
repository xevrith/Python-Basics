# Number Calculator

try:
    num1 = float(input("Enter a number : "))
    num2 = float(input("Enter another number : "))
    total = num1 + num2
    print(f"Total : {total}")
except ValueError:
    print("Invalid Number")