class Car:
    color = "Blue"
    def __init__(self,name,speed):
        self.name = name
        self.speed = speed


    def show_info(self):
        print(f"Name : {self.name} | Speed : {self.speed} | Color : {self.color}")


c1 = Car("BMW",200)
c1.show_info()

Car.color = "Red"
c1.show_info()