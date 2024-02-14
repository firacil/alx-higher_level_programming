#!/usr/bin/python3
"""
defining class TestRectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class to test rectangle
    """

    def test_attr(self):
        """
        testing attributes of rectangle
        """
        rectangle = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 100)
