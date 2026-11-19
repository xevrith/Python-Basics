import re
text = "cat ccdot cut c@t"
print(re.findall(r"c.t",text))
print(re.findall(r"c...t",text))

text = "cat cut cot cit"
print(re.findall(r"c.t",text))

text = "abc a1c a c abbc"
print(re.findall(r"a.c",text))

text = "start smart sport"
print(re.findall(r"s...t",text))

text = "a quick brown fox \njumps over a lazy dog"
print(re.findall(r"a.*dog",text,re.DOTALL))


text = "I love Python. I love SQL. I love Excel."
print(re.findall(r"I......Excel",text))

import re

text = """Hello Python
Welcome to Data Science"""
print(re.findall(r"Hello.*Science",text,re.DOTALL))

import re

text = """Name: Max
Age: 22
City: Jaipur
Course: Data Science"""
print(re.findall(r"Name.*Science",text,re.DOTALL))

import re

text = """Employee: Rahul
Department: IT
Salary: 40000

Employee: Aman
Department: HR
Salary: 35000"""

result = re.findall(r"Employee.*35000",text,re.DOTALL)
print(*result,sep="\n")