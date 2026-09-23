password = "python@123"
run = 1

while run <= 3:
    
    print(f"Hello User No. : {run}")
    attempts = 3

    while attempts >= 1:
        guess_password = input("Enter the password : ")

        if guess_password == password:
            print("Login Successful")
            break
        else:
            print("Try again")
        attempts -= 1

        if attempts == 0:
            print("Account Locked")
        else:
            print(f"Number of Attempts Left : {attempts}")

    run += 1
