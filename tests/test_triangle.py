import pytest

from src.Figure import Figure
from src.Triangle import Triangle


class Test_Triangle():

    def test_check_parent_class(self):
        assert issubclass(Triangle, Figure)

    def test_check_attribute_name(self):
        assert getattr(Triangle, 'name') == 'Triangle'

    def test_check_area(self, triangle):
        assert triangle.calculate_area == 84

    def test_check_perimeter(self, triangle):
        assert triangle.calculate_perimeter == 42

    def test_check_add_area_square(self, triangle, square):
        assert triangle.add_area(square) == 184

    def test_check_add_area_rectangle(self, triangle, rectangle):
        assert triangle.add_area(rectangle) == 234

    def test_check_add_area_circle(self, triangle, circle):
        assert triangle.add_area(circle) == 398
