#  program to check if the given string is a palindrome.

word = input("Enter a word : ")
reverse_word = ""

for i in word:
    reverse_word = i + reverse_word

if reverse_word == word:
    print(f"Given String is Palindrome")
else:
    print("Not a Palindrome")
