# Student Detail 

class Student:

    school_name = "ABC"

    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks

    def show_info(self):
        print(f"Student Name : {self.name}")
        print(f"Student Total : {sum(self.marks)}")
        print(f"Student Avg Marks : {sum(self.marks)/ len(self.marks)}")



s1 = Student("Tony",[20,30,50,10])
s2 =  Student("Stark",[60,80,90,99])

s2.show_info()
print()
s1.show_info()
