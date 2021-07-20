from src.Figure import Figure
from src.Rectangle import Rectangle
from src.Circle import Circle
from src.Triangle import Triangle


class Square(Figure):
    name = 'Square'

    def __init__(self, height):
        self.height = height
        # self.width = width
        super().__init__(name='Square', area=None, perimeter=None)

    @property
    def calculate_perimeter(self):
        self.perimeter = 4 * self.height
        return self.perimeter

    @property
    def calculate_area(self):
        self.area = self.height ** 2
        return self.area


# *** Вычисление площади и периметра квадрата ***
square = Square(20)
square_area = square.calculate_area
square_perimeter = square.calculate_perimeter

# *** Метод add_area(rectangle) ***
rectangle = Rectangle(15, 5)
square_add_rectangle = square.add_area(rectangle)

# *** Метод add_area(circle) ***
circle = Circle(10)
square_add_circle = square.add_area(circle)

# *** Метод add_area(triangle) ***
triangle = Triangle(13, 14, 15)
square_add_triangle = square.add_area(triangle)
