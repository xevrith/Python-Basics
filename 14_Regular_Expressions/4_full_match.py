import re

text = "96824"
text2 = "96824a"

print(re.fullmatch(r"\d{5}",text))
print(re.fullmatch(r"\d{5}",text2))