# Many Objects from One Class

class Car:
    brand_name = "BMW"

    def __init__(self,brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price



c1 = Car("BMW","X5",7500000)
print(f"Brand : {c1.model} | Model : {c1.model} | Price : {c1.price}")

c2 = Car("BMW","i14",600000)
print(f"Brand : {c2.model} | Model : {c2.model} | Price : {c2.price}")

c2.price = 500000
print(c2.price)