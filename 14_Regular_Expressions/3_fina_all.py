import re

text = "Python123"
print(re.findall(r"\d",text))
print(re.findall(r"\w",text))
print(re.findall(r"[aeiou]",text))

text2 = "a1b2c3"
print(re.findall(r"\d",text2))
print(re.findall(r"[^0-9]",text2))

text3 = "a b c"
print(re.findall(r"\s",text3))
