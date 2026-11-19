import re
text = "Order 101 shipped to Jaipur on 12-11-2026. Order 102 is pending."

print(re.search(r"\d+",text).group())
print(re.match(r"Order",text))
print(re.findall(r"\d{3}",text))
