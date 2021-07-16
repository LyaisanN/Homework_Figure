from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle


class Square(Figure):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        super().__init__(Square, area=None, perimeter=None)

    def add_area(self, another_figure):
        if not isinstance(Figure, another_figure):
            raise ValueError
        else:
            return square.calculate_area + another_figure.calculate_area


square = Square(10, 10)
square_area = square.calculate_area
square_perimeter = square.calculate_perimeter
rectangle = Rectangle(15, 5)
circle = Circle(10)
square_add_rectangle = square.add_area(circle)
print(square_perimeter)
print(square_area)
print(square_add_rectangle)
