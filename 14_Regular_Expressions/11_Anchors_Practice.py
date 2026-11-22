import re

text = """Python is easy to learn
Python is powerful
I am learning Python
Data Science is interesting
Python helps in AI
I love Python"""

print(re.search(r"^Python",text).group())
print(re.search(r"Python$",text).group())
print(re.search(r"Python$", text).group())