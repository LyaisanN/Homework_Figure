from src.Figure import Figure


class Rectangle(Figure):

    def __init__(self, height, width):
        self.height = height
        self.width = width
        super().__init__(Rectangle, area=None, perimeter=None)


rectangle = Rectangle(15, 10)
rectangle_area = rectangle.calculate_area
rectangle_perimeter = rectangle.calculate_perimeter
