# Compress data using run-length encoding: each character followed by the number of times it repeats
# consecutively. Print the compressed string.

data = "aabbbcccd"

a,b,c,d = 0,0,0,0

for char in data.lower():
    if char == "a":
        a += 1
    elif char == "b":
        b += 1
    elif char == "c":
        c += 1
    elif char == "d":
        d += 1


print(f"a{a}b{b}c{c}d{d}")