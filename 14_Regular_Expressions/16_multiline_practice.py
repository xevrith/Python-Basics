import re

# Question:
# Each employee record is on a separate line and begins with "Employee:".
# Find all employee names using ^ and the MULTILINE flag.
# Do not match text that appears in the middle of a line.

employee_records = """Employee: Aisha
Department: Sales
Employee: Rahul
Department: IT
Note: Employee: Meera is a contractor
Employee: Kabir
Department: Finance"""

# Answer:
employee_names = re.findall(r"^Employee:\s*(.+)$", employee_records, re.MULTILINE)
print(employee_names)
