"""
FILE HANDLING PRACTICE 05: Attendance Report

Scenario:
A teacher stores student attendance in a text file.
Each line contains a student name and attendance status.

PRACTICE TASKS
1. Create attendance.txt with these records:
   Aisha,Present
   Rahul,Absent
   Neha,Present
   Kabir,Present
   Sara,Absent
2. Read the file line by line.
3. Count present and absent students.
4. Display the names of absent students.
5. Display the total number of students.

Try solving the tasks yourself before checking the answers.
"""

# -------------------- ANSWERS --------------------

# Answer 1: Create the attendance file.
with open("attendance.txt", "w") as file:
    file.write("Aisha,Present\n")
    file.write("Rahul,Absent\n")
    file.write("Neha,Present\n")
    file.write("Kabir,Present\n")
    file.write("Sara,Absent\n")

# Answer 2: Read all records.
with open("attendance.txt", "r") as file:
    records = file.read().splitlines()

present_count = 0
absent_count = 0

print("Absent students:")

# Answers 3 and 4: Count attendance and list absent students.
for record in records:
    name, status = record.split(",")

    if status == "Present":
        present_count += 1
    elif status == "Absent":
        absent_count += 1
        print(name)

# Answer 5: Display the summary.
print("Present:", present_count)
print("Absent:", absent_count)
print("Total students:", len(records))
