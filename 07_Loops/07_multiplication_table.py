# program to print a multiplication table of a given number

table_num = int(input("Enter the table number : "))

for num in range(1,11):
    if num == 10:
        print(f"{table_num} x {num} = {table_num * num}")
        break
    else:
        print(f"{table_num} x {num} = {table_num * num}")