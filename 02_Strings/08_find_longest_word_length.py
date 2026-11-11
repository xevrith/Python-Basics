sentence = "Python is a powerful programming language".split()
length = []

for word in sentence:
    length.append(len(word))

print(f"{max(length)}")
       