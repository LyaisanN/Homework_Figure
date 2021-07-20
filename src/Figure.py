class Figure:
    height = None
    width = None

    def __init__(self, name, area, perimeter):
        self.name = name
        self.area = area
        self.perimeter = perimeter

    @property
    def calculate_area(self):
        return self.height * self.width

    @property
    def calculate_perimeter(self):
        return 2 * (self.height + self.width)

    def add_area(self, another_figure):
        if isinstance(another_figure, Figure):
            return self.calculate_area + another_figure.calculate_area
        else:
            raise ValueError('Invalid class!')
