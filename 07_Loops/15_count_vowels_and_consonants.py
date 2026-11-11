sentance = "Loops are Fun!"
vowels = ("aeiou")
v_count = 0
c_count = 0

for char in sentance.lower():
    if char.isalpha():
        if char in vowels:
            v_count += 1
        else:
            c_count += 1


print(f"V count : {v_count}")
print(f"C count : {c_count}")