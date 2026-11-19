import re

s1 = "Hello world"
s2 = "Say Hello"

print(re.match(r"Hello",s1).group())
print(re.findall(r"^Hello",s1))
print(re.search(r"^Hello",s1).group())
print(re.search(r"^Hello",s2))

f1 = "report.pdf"
f2 = "pdf.txt"

print(re.search(r".pdf$",f1).group())
print(re.findall(r".pdf$",f2))

text = "cat category concatenate cat"
print(re.findall(r"\bcat\b",text))
print(re.findall(r"\Bcat\B",text))