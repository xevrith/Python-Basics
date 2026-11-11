# Age Input

try:
    age = int(input("Enter Your Age : "))
    print(f"Your Age : {age}")
except ValueError:
    print("Invalid Age")