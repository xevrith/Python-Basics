word = "pythonista"
new_word = ""
idx = 0

for char in word:
    if idx % 2 == 0:
        new_word += char.upper()
    else:
        new_word += char.lower()
    idx += 1

print(new_word)
