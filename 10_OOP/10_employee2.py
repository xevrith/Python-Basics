class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def monthly_salary(self):
        return self.salary / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, salary,days):
        super().__init__(name, salary)
        self.days = days

    def monthly_salary(self):
        return self.salary * self.days

e1 = FullTimeEmployee("Alice", 60000)
e2 = PartTimeEmployee("Bob", 500, 20)

print(f"{e1.name} salary : {e1.monthly_salary()}")
print(f"{e2.name} salary : {e2.monthly_salary()}")

