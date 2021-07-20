import pytest

from src.Figure import Figure
from src.Circle import Circle


class Test_Circle():

    def test_check_parent_class(self):
        assert issubclass(Circle, Figure)

    def test_check_attribute_name(self):
        assert getattr(Circle, 'name') == 'Circle'

    def test_check_area(self, circle):
        assert circle.calculate_area == 314

    def test_check_perimeter(self, circle):
        assert circle.calculate_perimeter == 62.8

    def test_check_add_area_square(self, circle, square):
        assert circle.add_area(square) == 414

    def test_check_add_area_rectangle(self, circle, rectangle):
        assert circle.add_area(rectangle) == 464

    def test_check_add_area_triangle(self, circle, triangle):
        assert circle.add_area(triangle) == 398
