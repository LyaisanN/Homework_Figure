import pytest

from src.Figure import Figure
from src.Square import Square


class Test_Square():

    def test_check_parent_class(self):
        assert issubclass(Square, Figure)

    def test_check_attribute_name(self):
        assert getattr(Square, 'name') == 'Square'

    def test_check_area(self, square):
        assert square.calculate_area == 100

    def test_check_perimeter(self, square):
        assert square.calculate_perimeter == 40

    def test_check_add_area_rectangle(self, square, rectangle):
        assert square.add_area(rectangle) == 250

    def test_check_add_area_triangle(self, square, triangle):
        assert square.add_area(triangle) == 184

    def test_check_add_area_circle(self, square, circle):
        assert square.add_area(circle) == 414
