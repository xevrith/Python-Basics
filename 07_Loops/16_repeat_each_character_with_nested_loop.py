# every character, print it 3 times on separate rows.

char = input("Enter a char : ")

for i in range(1,4):
    for j in char:
        print(j,end=" ")
    print()