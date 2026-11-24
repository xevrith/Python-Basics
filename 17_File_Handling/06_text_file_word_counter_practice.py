"""
FILE HANDLING PRACTICE 06: Text File Word Counter

Scenario:
You receive a short text file and need to calculate basic text statistics.

PRACTICE TASKS
1. Create notes.txt with at least three sentences.
2. Read the complete file content.
3. Count the total number of words.
4. Count how many times the word "python" appears (ignore letter case).
5. Display the total number of characters, excluding leading and trailing spaces.

Try solving the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1: Create a sample text file.
with open("notes.txt", "w") as file:
    file.write("Python is useful for data analysis.\n")
    file.write("I am learning Python every day.\n")
    file.write("Practice makes Python easier to understand.\n")

# Answer 2: Read the complete file.
with open("notes.txt", "r") as file:
    content = file.read()

# Answer 3: Count all words.
words = content.split()
print("Total words:", len(words))

# Answer 4: Count occurrences of Python, ignoring letter case.
python_count = content.lower().split().count("python")
print("Occurrences of 'python':", python_count)

# Answer 5: Count characters after removing outer whitespace.
print("Total characters:", len(content.strip()))
