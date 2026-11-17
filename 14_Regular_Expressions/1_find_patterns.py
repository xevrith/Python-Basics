import re

result = re.search(r"dog","my dog is big")
print(result)
print(result.group())

result2 = re.search(r"fish", "I like cats")
print(result2)

result3 = re.search(r"2026","Year is 2026")
print(result3)
print(result3.group())  

result4 = re.search(r"Python","I love Python")

if result4:
    print("Found")

