# Classroom

class Classroom:
    def __init__(self,teacher):
        self.teacher = teacher
        self.student = []

    def add_student(self,students):
        self.student.append(students)
        print("Student added successfully")

    def show_students(self):
        for stud in self.student:
            print(stud)


class MathClass(Classroom):

    def total_students(self):
        print(len(self.student))

    def is_enrolled(self,name):
        if name in self.student:
            return True
        else:
            False

    def show_teacher(self):
        print(self.teacher)


m = MathClass("Mr. Khan")
m.add_student("Ali")
m.add_student("Sara")
m.add_student("Zoya")

m.show_teacher()
m.show_students()
m.total_students()
print(m.is_enrolled("Sara"))
print(m.is_enrolled("Imran"))
