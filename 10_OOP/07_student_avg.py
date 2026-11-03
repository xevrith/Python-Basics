class Student:

    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    def avg(self):
        print(f"Name : {self.name} | Average : {sum(self.marks) / len(self.marks)}")


s1 = Student("Alice", [85, 90, 78, 92, 88])
s1.avg()