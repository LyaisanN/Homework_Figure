from src.Figure import Figure


class Rectangle(Figure):
    name = 'Rectangle'

    def __init__(self, height, width):
        self.height = height
        self.width = width
        super().__init__(name='Rectangle', area=None, perimeter=None)


# *** Вычисление площади и периметра прямоугольника ***
rectangle = Rectangle(15, 10)
rectangle_area = rectangle.calculate_area
rectangle_perimeter = rectangle.calculate_perimeter
