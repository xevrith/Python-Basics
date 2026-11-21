import re
text = "<div>Hello</div><span>World</span>"
print(re.findall(r">(.*?)<",text))

s = "aaaa"
print(re.search(r"a+?",s).group())
