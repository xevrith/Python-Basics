# calculate the sum of all numbers from 1 to a given number.

n = int(input("Enter number :"))
total = 0

for i in range(1,n + 1):
    total += i

print(f"Total : {total}")