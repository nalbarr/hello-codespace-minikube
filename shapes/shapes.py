# -*- coding: utf-8 -*-


class BaseShape:
    """
    BaseShape
    """

    name = ""

    def __init__(self, name):
        self.name = name

    def get_name(self):
        """
        BaseShape.get_name()
        """
        return self.name


class Square(BaseShape):
    """
    Square
    """

    side = 0.0

    def __init__(self, name, side):
        self.side = side
        super().__init__(name)

    def get_area(self):
        """
        Square.get_area
        """
        area = self.side * self.side
        return area


class Triangle(BaseShape):
    """
    Triangle
    """

    base = 0.0
    height = 0.0

    def __init__(self, name, base, height):
        self.base = base
        self.height = height
        super().__init__(name)

    def get_area(self):
        """
        Triangle.get_area
        """
        area = 0.5 * self.base * self.height
        return area
