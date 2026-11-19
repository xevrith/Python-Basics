import re

text = "I have 2 cats and 3 dogs"

print(re.findall(r"\d",text))
print(re.findall(r"[A-Za-z]+",text))
print(re.findall(r"^I",text))
print(re.findall(r"dogs$",text))
print(re.findall(r"\bcats\b",text))

text = "Rahul paid 500 and Aman paid 1200"
print(re.findall(r"\d+",text))
print(re.findall(r"[a-zA-Z]+",text))

text = "education"
print(re.findall(r"[aeiou]",text))

