class Temp:
    def __init__(self,celsius):
        self.celsius = celsius 

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32


    def to_kelvin(self):
        return self.celsius * 273.15


t = Temp(100)
print(f"Fahrenheit : {t.to_fahrenheit()}")
print(f"Kelvin : {t.to_kelvin()}")