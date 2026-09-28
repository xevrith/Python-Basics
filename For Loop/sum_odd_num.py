#  calculate the sum of all the odd numbers within the given range.

n = int(input("Enter number : "))
total = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        total += i
    else:
        continue

print(f"Total : {total}")