from src.Figure import Figure


class Triangle(Figure):
    name = 'Triangle'

    def __init__(self, height_1, height_2, width):
        if height_1 + height_2 < width or height_1 + width < height_2 or height_2 + width < height_1:
            raise AttributeError('None')
        self.height_1 = height_1
        self.height_2 = height_2
        self.width = width
        super().__init__(name='Triangle', area=None, perimeter=None)

    @property
    def calculate_perimeter(self):
        self.perimeter = self.height_1 + self.height_2 + self.width
        return self.perimeter

    @property
    def calculate_area(self):
        P = (self.height_1 + self.height_2 + self.width) / 2
        self.area = int((P * (P - self.height_1) * (P - self.height_2) * (P - self.width)) ** 0.5)
        return self.area


# *** Вычисление площади и периметра треугольника ***
triangle = Triangle(13, 14, 15)
triangle_perimeter = triangle.calculate_perimeter
triangle_area = triangle.calculate_area
