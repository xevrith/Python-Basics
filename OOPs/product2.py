class Product:

    def __init__(self,name,price):
        self.name = name 
        self.price = price 

class Clothing(Product):
    def __init__(self, name, price,size):
        super().__init__(name, price)
        self.size = size 



p1 = Clothing("T-shirt",299,"XL")
print(p1.name,p1.price,p1.size)

    