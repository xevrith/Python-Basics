# Division

try:
    num1 = float(input("Enter a number : "))
    num2 = float(input("Enter a number : "))
    total = num1 / num2

except ZeroDivisionError:
    print("Divided By Zero Try again")