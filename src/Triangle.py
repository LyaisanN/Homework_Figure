from src.Figure import Figure


class Triangle(Figure):

    def __init__(self, height_1, height_2, width):
        self.height_1 = height_1
        self.height_2 = height_2
        self.width = width
        super().__init__(Triangle, area=None, perimeter=None)

    def calculate_triangle_perimeter(self):
        self.perimeter = self.height_1 + self.height_2 + self.width
        return self.perimeter

    def calculate_triangle_area(self):
        P = (self.perimeter)/2
        self.area = int((P * (P - self.height_1) * (P - self.height_2) * (P - self.width)) ** 0.5)
        return self.area


triangle = Triangle(13, 14, 15)
triangle_perimeter = triangle.calculate_triangle_perimeter()
triangle_area = triangle.calculate_triangle_area()

