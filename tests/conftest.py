import pytest

from src.Square import Square
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Circle import Circle


@pytest.fixture()
def square():
    square = Square(height=10)
    yield square
    del square


@pytest.fixture()
def rectangle():
    rectangle = Rectangle(height=10, width=15)
    yield rectangle
    del rectangle


@pytest.fixture()
def triangle():
    triangle = Triangle(height_1=13, height_2=14, width=15)
    yield triangle
    del triangle


@pytest.fixture()
def circle():
    circle = Circle(radius=10)
    yield circle
    del circle
