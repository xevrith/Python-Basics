#  Basic Sum In loop
total = 0

while True:
    try:
        num1 = int(input("Enter a number : "))
        
        if num1 == 0:
            break
        else:
            total += num1
            print("Number added")
    except ValueError as e:
        print("Value Error",e)

print(f"Total : {total}")