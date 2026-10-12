#The formula for finding the area of ​​a circle and a class constructed using A = πr².

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print(f"{area}")

r = Circle(7)

r.calculate_area()