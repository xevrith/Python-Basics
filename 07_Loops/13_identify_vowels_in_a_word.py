# each character, check whether it is vowel or not

char = input("Enter a Word : ").lower()

for i in char:
    if i == "a" or  i == "e" or i == "i" or i == "o" or i == "u":
        print(f"{i.upper()} : Vowel")
    else:
        print(f"{i.upper()} : Not Vowel")