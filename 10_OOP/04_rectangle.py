# Find the area of a rectangle

class Rectangle:

    def __init__(self,length, width):
        self.length = length
        self.width = width 

    def area(self):
        return f"The area of a rectangle is {self.length * self.width}"



r1 = Rectangle(20,30)
r2 = Rectangle(50,60)

