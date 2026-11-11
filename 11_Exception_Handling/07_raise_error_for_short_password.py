# Password Length

password = input("Enter a password : ")

if len(password) < 6:
    raise ValueError("Enter a strong password")
else:
    print("Password accepted")

    