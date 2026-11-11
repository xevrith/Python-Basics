# Given words = ["apple", "kiwi", "banana", "fig"], use filter() and a lambda to keep only words with more than 4 letters.

words = ["apple", "kiwi", "banana", "fig"]
clean_word = list(filter(lambda word:len(word) > 4,words))
print(clean_word)