class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary 

    def display(self):
        print(f"Name : {self.name} | Salary: {self.salary}")

    def increase_salary(self,percentage):
        if percentage > 0:
            bonus = self.salary * percentage
            total_salary = self.salary + bonus
            print(f"Final Salary : {total_salary}")

        else:
            print("Invalid Input")


e1 = Employee("Max",30000)
e2 = Employee("Ali",40000)

e1.display()
e2.display()

e1.increase_salary(0.10)
e2.increase_salary(0.15)

e1.display()
e2.display()

e2.increase_salary(-0.05)