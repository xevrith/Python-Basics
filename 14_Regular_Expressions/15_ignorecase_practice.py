import re

# Question:
# A system stores status values with inconsistent capitalization.
# Find every occurrence of "approved" regardless of letter case.
# Use the IGNORECASE flag.

status_log = """
Request 101: APPROVED
Request 102: pending
Request 103: Approved
Request 104: rejected
Request 105: approved
"""

# Answer:
approved_statuses = re.findall(r"approved", status_log, re.IGNORECASE)
print(approved_statuses)
