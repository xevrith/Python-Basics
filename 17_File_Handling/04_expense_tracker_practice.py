"""
FILE HANDLING PRACTICE 04: Expense Tracker

Scenario:
You are tracking daily expenses in a text file.

PRACTICE TASKS
1. Create expenses.txt and write these records, one per line:
   Food,250
   Travel,80
   Books,450
   Snacks,120
2. Read the records from the file.
3. Calculate the total amount spent.
4. Find and display expenses greater than 100.
5. Display the number of expense records.

Try solving the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1: Create the expense file.
with open("expenses.txt", "w") as file:
    file.write("Food,250\n")
    file.write("Travel,80\n")
    file.write("Books,450\n")
    file.write("Snacks,120\n")

# Answer 2: Read all records.
with open("expenses.txt", "r") as file:
    expenses = file.read().splitlines()

total_spent = 0

# Answers 3 and 4: Calculate total and show expenses above 100.
print("Expenses above 100:")
for expense in expenses:
    category, amount_text = expense.split(",")
    amount = int(amount_text)
    total_spent += amount

    if amount > 100:
        print(category, amount)

# Answer 5: Display the summary.
print("Total spent:", total_spent)
print("Number of expense records:", len(expenses))
