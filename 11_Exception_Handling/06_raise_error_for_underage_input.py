# Age Validation

age = int(input("Enter your age : "))

if age < 18:
    raise ValueError("Age must be greater then or equal to 18")
else:
    print(age)