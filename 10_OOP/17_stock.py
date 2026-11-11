class Product:

    def __init__(self,name, price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

p1 = Product("Laptop", 899.99, 5)
print(f"Total stock value of Laptop: ${p1.total_value()}")