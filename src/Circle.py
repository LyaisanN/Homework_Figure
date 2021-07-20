from src.Figure import Figure


class Circle(Figure):
    name = 'Circle'

    def __init__(self, radius):
        self.radius = radius
        super().__init__(name='Circle', area=None, perimeter=None)

    @property
    def calculate_perimeter(self):
        pi = 3.14
        self.perimeter = round(2 * self.radius * pi, 1)
        return self.perimeter

    @property
    def calculate_area(self):
        pi = 3.14
        self.area = pi * (self.radius ** 2)
        return self.area


# *** Вычисление площади и длины окружности круга ***
circle = Circle(10)
circle_perimeter = circle.calculate_perimeter
circle_area = circle.calculate_area
