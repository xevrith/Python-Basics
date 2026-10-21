class BankAccount:
    def __init__(self,name, balance):
        self.name = name
        self.__balance = balance 

    def display_balance(self):
        return self.__balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("Insufficint Balance")

    def add_amount(self,amount):
        if amount > 0:
            self.__balance += amount

class SavingAccount(BankAccount):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def add_intrest(self,intrest):
        intrest_amount = self.display_balance() * intrest
        self.add_amount(intrest_amount)



c1 = SavingAccount("Max",5000)
print(f"Balance : {c1.display_balance()}")
c1.deposit(3000)
print(f"Balance : {c1.display_balance()}")
c1.withdraw(3000)
print(f"Balance : {c1.display_balance()}")
c1.add_intrest(0.5)
print(f"Balance : {c1.display_balance()}")

