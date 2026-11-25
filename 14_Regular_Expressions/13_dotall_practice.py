import re

# Question:
# A support ticket contains a message split across multiple lines.
# Extract everything between <message> and </message>, including newlines.
# Use the DOTALL flag.

ticket = """Ticket: 1042
<message>
The application crashes
when I upload a large file.
Please investigate.
</message>
Status: Open"""

# Answer:
message = re.search(r"<message>(.*?)</message>", ticket, re.DOTALL)

if message:
    print(message.group(1).strip())
