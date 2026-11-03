class Car:

    def __init__(self):
        self.is_on = False 

    def turn_on(self):
        self.is_on =  True 

    def turn_off(self):
        self.is_on = False 

    def status(self):
        state = "Car is On" if self.is_on == True else "Car is Off"
        print(state)


c1 = Car()
c1.turn_on()
c1.status()
c1.turn_off()
c1.status()