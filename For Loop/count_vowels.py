# Count how many vowels are there in a sentance 

sentance = input("Enter a sentance : ").lower()
count = 0

for vowels in sentance:
    if "a" in vowels or "e" in vowels or "i" in vowels or "o" in vowels or "u" in vowels:
        count += 1


print(f"Total Vowels : {count}")