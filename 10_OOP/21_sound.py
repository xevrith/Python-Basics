class Animal:
    def __init__(self,name):
        self.name = name
    def speak():
        print("Speaking")


class Dog(Animal):
    def speak(self):
        print(f"{self.name} Woof Woof")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} Meow Meow")


c1 = Cat("Cat")
c1.speak()
d1 = Dog("Bruno")
d1.speak()