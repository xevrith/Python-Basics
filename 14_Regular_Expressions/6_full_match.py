import re

text1 = "302012"
text2 = "302012a"

print(re.fullmatch(r"\d{6}",text1).group())
print(re.fullmatch(r"\d{6}",text2))

pin = "12345"
print("Valid" if re.fullmatch(r"\d{5}",pin) else "Invalid")

pin2 = "12a345"
print("Valid" if re.fullmatch(r"\d{5}",pin2)else "Invalid")

phone_number = "9874563210"
print("Valid" if re.fullmatch(r"\d{10}",phone_number) else "Invalid")

