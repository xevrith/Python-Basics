num = 75869
count = 0

while num != 0:
    # Floor division to remove the last digit
    num = num // 10
    # Increment the counter
    count = count + 1

print("Total digits are:", count)
