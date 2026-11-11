email = "student.name@college.edu"
new_email = list(email.rpartition("@"))
second_email = new_email[-1].split(".")

new_email.remove("@")
new_email.remove("college.edu")
new_email.extend(second_email)

for item in new_email:
    print(item)