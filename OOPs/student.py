# Student name 

class Student:

    def __init__(self, fullname, marks):
        self.fullname = fullname
        self.marks = marks
        print("Adding new student in database")


s1 = Student("Alice", 450)
print(s1.fullname)
print(s1.marks)

s2 = Student("Bob", 599)
print(s2.fullname)
print(s1.marks)
