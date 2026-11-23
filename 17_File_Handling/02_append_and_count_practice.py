"""
FILE HANDLING PRACTICE 02: Appending and Counting

Topics:
- Append mode ("a")
- readlines()
- len()
- strip()

PRACTICE TASKS
1. Create a file named "daily_tasks.txt" and write three tasks.
2. Append two more tasks without deleting the existing content.
3. Read all lines from the file.
4. Display how many tasks are stored in the file.
5. Display each task with its line number.

Try the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1: Create the file and write the first three tasks.
with open("daily_tasks.txt", "w") as file:
    file.write("Practice Python\n")
    file.write("Revise SQL\n")
    file.write("Read a chapter\n")

# Answer 2: Append two tasks.
with open("daily_tasks.txt", "a") as file:
    file.write("Complete an Excel task\n")
    file.write("Review today's notes\n")

# Answer 3: Read all lines.
with open("daily_tasks.txt", "r") as file:
    tasks = file.readlines()

# Answer 4: Count the tasks.
print("Total tasks:", len(tasks))

# Answer 5: Display each task with its line number.
for number, task in enumerate(tasks, start=1):
    print(number, task.strip())
