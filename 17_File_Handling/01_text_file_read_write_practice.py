"""
FILE HANDLING PRACTICE 01: Writing and Reading a Text File

Topics:
- open()
- write()
- read()
- with open()
- File modes: "w" and "r"

PRACTICE TASKS
1. Create a file named "student.txt".
2. Write the student's name, age, and course into the file.
3. Read the complete contents of the file and display them.
4. Read the file again and display only the first line.

Try the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1 and 2: Create the file and write student details.
with open("student.txt", "w") as file:
    file.write("Name: Max\n")
    file.write("Age: 22\n")
    file.write("Course: Data Science\n")

# Answer 3: Read and display the complete file.
with open("student.txt", "r") as file:
    content = file.read()
    print("Complete file content:")
    print(content)

# Answer 4: Read and display only the first line.
with open("student.txt", "r") as file:
    first_line = file.readline()
    print("First line:", first_line)
