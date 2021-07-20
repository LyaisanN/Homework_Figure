import pytest

from src.Figure import Figure
from src.Rectangle import Rectangle


class Test_Rectangle():

    def test_check_parent_class(self):
        assert issubclass(Rectangle, Figure)

    def test_check_attribute_name(self):
        assert getattr(Rectangle, 'name') == 'Rectangle'

    def test_check_area(self, rectangle):
        assert rectangle.calculate_area == 150

    def test_check_perimeter(self, rectangle):
        assert rectangle.calculate_perimeter == 50

    def test_check_add_area_square(self, rectangle, square):
        assert rectangle.add_area(square) == 250

    def test_check_add_area_triangle(self, rectangle, triangle):
        assert rectangle.add_area(triangle) == 234

    def test_check_add_area_circle(self, rectangle, circle):
        assert rectangle.add_area(circle) == 464
