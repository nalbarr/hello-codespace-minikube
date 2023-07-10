import pytest

import shapes
from shapes import Square as square
from shapes import Triangle as triangle


@pytest.fixture
def square():
    square = shapes.Square("square1", 2.0)
    return square


@pytest.fixture
def triangle():
    triangle = shapes.Triangle("triangle1", 4.0, 1.0)
    return triangle


def test_square(square):
    expected = 4.0
    actual = square.get_area()
    assert actual == expected


def test_triangle(triangle):
    expected = 2.0
    actual = triangle.get_area()
    assert actual == expected
