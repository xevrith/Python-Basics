class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.price = price 
        self.stock = stock

    def display(self):
        print(f"Product Name : {self.name}")
        print(f"Product Price : {self.price}")
        print(f"Product Stocks : {self.stock}")

    def sell(self,quantity):

        if quantity <= 0:
            print("Invalid Quantity")

        else:
            if quantity <= self.stock:
                self.stock -= quantity
                print(f"Purchase Successfully")

            else:
                print("Insufficient Stock")

    def restock(self,quantity):
        if quantity <= 0:
            print("Invalid Quantity")

        else:
            self.stock += quantity
            print("stock added successfully")


p1 = Product("Milk",26, 10)
p1.display()

p1.sell(6)
p1.display()
p1.sell(9)
p1.restock(20)
p1.display()