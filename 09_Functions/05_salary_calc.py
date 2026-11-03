# Employee Salary Calculator

def salary_calc(salary, bonus, months=12):

        annual_salary = salary * months
        annual_bonus = bonus * months
        final_salary = annual_salary + annual_bonus

        return final_salary

   
try:
    emp_salary = int(input("Enter Your salary : "))
    emp_bonus = int(input("Enter Bonus : "))
    print(f"Annual Salary : {salary_calc(emp_salary,emp_bonus)}")

except ValueError:
    print("Wrong Input")
