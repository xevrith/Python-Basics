class Payment:
    def __init__(self,amount):
        self.amount = amount

    def pay(self):
        print(f"Processing payment of {self.amount}")


class CreditCard(Payment):
    def pay(self):
        print(f"Processing Payment of {self.amount} with 2% FEE")
        

class UPIPayment(Payment):
    def pay(self):
        print(f"Processing Payment of {self.amount} with NO FEE")

c1 = CreditCard(3000)
c1.pay()

c2 = UPIPayment(5000)
c2.pay()