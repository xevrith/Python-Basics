import re

text = "regular expressions"
print(re.findall(r"[a-z]+",text))

text = "Rahul and Aman went to Jaipur"
print(re.findall(r"[A-Z]",text))

text = "a1b2c3"
print(re.findall(r"[a-z]",text))

text = "Room 45, Floor 3"
print(re.findall(r"[0-9]+",text))

