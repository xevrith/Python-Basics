import re

# Question:
# Extract each HTML-like tag's content separately from the text below.
# First demonstrate why a greedy pattern is unsuitable, then use a
# non-greedy pattern to get the two separate matches.

html = "<h1>Python Basics</h1><p>Learn regular expressions</p>"

# Answer: Greedy matching takes the longest possible match.
greedy_result = re.findall(r"<.*>(.*)<.*>", html)
print("Greedy:", greedy_result)

# Answer: Adding ? makes the quantifier non-greedy.
non_greedy_result = re.findall(r"<.*?>(.*?)</.*?>", html)
print("Non-greedy:", non_greedy_result)
