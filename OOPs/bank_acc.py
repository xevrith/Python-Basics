# Bank Account

class BankAccount:
    bank_name = "HDFC"

    def __init__(self,balance):
        self._balance = balance #protected
        self.__acc = 123456789 #private


    def credit(self,amount):
        self._balance += amount 
        print(f"Amount added {amount} : Current Balance {self._balance}")


    def debit(self,amount,account_number):
        if account_number == self.__acc:
            if amount > self._balance:
                print("Insufficint Balance")
            else:
                self._balance -= amount 
                print(f"Amount {amount} : Current Balance {self._balance}")

        else:
            print(f"Wrong Account Number")


acc1 = BankAccount(5000)
acc1.credit(3000)

acc1.debit(2000,123456789)