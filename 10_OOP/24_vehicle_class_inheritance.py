# Inheritance Practice:Vehicle and Car

class Vehicle:
    def __init__(self,brand):
        self.brand = brand 

    def show_brand(self):
        print("Brand Name",self.brand)


class Car(Vehicle):
    def honk(self):
        print(f"{self.brand} says beep beep")


c = Car("BMW")
c.show_brand()
c.honk()

