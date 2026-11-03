# program to count the total number of digits in a number.

number = input("Enter number : ")
count = 0

for i in number:
    count += 1

print(f"Total Number : {count}")