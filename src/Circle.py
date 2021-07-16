from src.Figure import Figure


class Circle:

    def __init__(self, radius):
        self.radius = radius
        # super().__init__(Circle, area=None, perimeter=None)

    def calculate_circle_perimeter(self):
        pi = 3.14
        self.perimeter = 2 * self.radius * pi
        return self.perimeter

    def calculate_circle_area(self):
        pi = 3.14
        self.area = int(pi * (self.radius ** 2))
        return self.area


circle = Circle(10)
circle_perimeter = circle.calculate_circle_perimeter()
circle_area = circle.calculate_circle_area()
