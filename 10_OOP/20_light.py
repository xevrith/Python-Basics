class Light:

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        self.is_on =  True

    def Turn_off(self):
        self.is_on = False


    def status(self):
        state = "Turn On" if self.is_on == True else "Turn Off"
        print(state)


light = Light()
light.turn_on()
light.status()
light.Turn_off()
light.status()