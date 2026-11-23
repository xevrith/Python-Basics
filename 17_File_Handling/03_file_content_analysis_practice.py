"""
FILE HANDLING PRACTICE 03: Basic File Content Analysis

Scenario:
You are given a small sales report stored in a text file.
Your task is to read the report and calculate basic summary information.

Topics:
- Reading files
- splitlines()
- split()
- int()
- for loops
- Accumulator variables

PRACTICE TASKS
1. Create "sales.txt" and write these records, one per line:
   Pen,10
   Notebook,25
   Pencil,5
   Marker,15
2. Read the file.
3. Calculate the total quantity sold.
4. Find the product with the highest quantity.
5. Display the number of product records.

Try the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1: Create the sample sales report.
with open("sales.txt", "w") as file:
    file.write("Pen,10\n")
    file.write("Notebook,25\n")
    file.write("Pencil,5\n")
    file.write("Marker,15\n")

# Answer 2: Read the file and convert its lines into a list.
with open("sales.txt", "r") as file:
    records = file.read().splitlines()

total_quantity = 0
highest_product = ""
highest_quantity = 0

# Answers 3 and 4: Calculate total quantity and find the highest record.
for record in records:
    product, quantity_text = record.split(",")
    quantity = int(quantity_text)

    total_quantity += quantity

    if quantity > highest_quantity:
        highest_quantity = quantity
        highest_product = product

# Answer 5: Display the summary.
print("Total quantity sold:", total_quantity)
print("Highest-selling product:", highest_product)
print("Highest quantity:", highest_quantity)
print("Number of product records:", len(records))
