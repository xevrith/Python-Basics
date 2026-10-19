class CoffeeMachine:

    def __init__(self,water,coffee,milk):
        self.water = water
        self.coffee = coffee
        self.milk = milk 

    def make_latte(self):
        if self.water >= 200 and self.coffee >= 20 and self.milk >= 150:
            print(f"Latte made! Remaining - Water: {self.water - 200}ml, Coffee: {self.coffee - 20}g, Milk: {self.milk - 150}")
        else:
            print("Not enough resources to make a latte.")

c1 = CoffeeMachine(300, 100, 200)
c1.make_latte()