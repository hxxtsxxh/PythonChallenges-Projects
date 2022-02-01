# get the area of a rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def getArea(self):
        units = input("What are the units [ft] [in] [m] [cm]: ")
        return str(self.height * self.width) + '' + units + "^2"


rect1 = Rectangle(50, 30)
print(rect1.getArea())
