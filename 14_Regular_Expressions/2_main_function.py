import re

text = "apple banana apple"

print(re.match(r"apple",text)) # Matches only at the start
print(re.match(r"banana",text))
print(re.findall(r"apple",text))
print(re.fullmatch(r"apple",text))
