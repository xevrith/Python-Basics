class Cart:

    company = "FlipClip"

    def __init__(self,product,category,price):
        self.product = product 
        self.category = category
        self.price = price 
        self.cart = {"Product" : self.product,"Category":self.category,"Price":self.price}

    

    def display_cart(self):
        for key,value in self.cart.items():
            print(f"{key} : {value}")

p1 = Cart("Smartphone","Electronic",30000.00)
p1.display_cart()


