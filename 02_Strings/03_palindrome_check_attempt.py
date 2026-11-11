text = "A man a plan a canal Panama"
reverse_text = ""

for char in text:
    reverse_text = reverse_text + char

if text == reverse_text:
    print(True)
else:
    print(False)