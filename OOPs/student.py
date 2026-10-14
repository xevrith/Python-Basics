class Student:

    school_name = "ABC"
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks 

    def avg(self):
        avg_marks = sum(self.marks) / len(self.marks)
        print(f"Average Marks : {avg_marks}")




s1 = Student("Alice",[50,60,40,90])
s1.avg()