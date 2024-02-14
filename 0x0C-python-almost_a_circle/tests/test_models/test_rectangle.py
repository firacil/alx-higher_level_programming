#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
'''
    defining class TestRectangle
'''


class test_rectangle(unittest.TestCase):
    '''
        class to test rectangle
    '''

    def test_startup(self):
        '''
        intialize instance width and height
        '''
        self.rec = Rectangle(4, 5)

    def test_teardown(self):
        '''
            delete created instances
        '''
        self.rec = Rectangle(4, 5)
        del self.rec

    def test_width(self):
        '''
            testing rectangles width getter
        '''
        self.rec = Rectangle(4, 5)
        self.assertEqual(4, self.rec.width)

    def test_height(self):
        '''
            testing rectangles height getter
        '''
        self.rec = Rectangle(4, 5)
        self.assertEqual(5, self.rec.height)

    def test_x(self):
        '''
            testing rectangle x getter
        '''
        self.rec = Rectangle(4, 5, 32)
        self.assertEqual(32, self.rec.x)

    def test_y(self):
        '''
            testing rectangles y getter
        '''
        self.rec = Rectangle(4, 5, 32, 64)
        self.assertEqual(64, self.rec.y)

    def test_width_type(self):
        '''
            testing when string recived by width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle("4", 5)

    def test_width_boo(self):
        '''
            let me test when bool passed to width
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(True, 5)

    def test_width_all(self):
        '''
            test when width over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle((1, 2), 5)

    def test_height_type(self):
        '''
            test when string passed to height
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, "5")

    def test_height_boo(self):
        '''
            check for typeerror when boolean passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, True)

    def test_height_all(self):
        '''
            check when another over data passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, [1, 2])

    def test_x_type(self):
        '''
            test x when string passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, "32")

    def test_x_boo(self):
        '''
            test when x passed as bool
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, True)

    def test_x_all(self):
        '''
            test when over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, [1, 2])

    def test_y_type(self):
        '''
            test when string passed as y
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, "64")

    def test_y_boo(self):
        '''
            test when y passed as bool
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, True)

    def test_y_all(self):
        '''
            test when over passed
        '''
        with self.assertRaises(TypeError):
            r = Rectangle(4, 5, 32, [64, 65])

    def test_width_val(self):
        '''
            test value of width
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(-4, 5)

    def test_height_val(self):
        '''
            test value of height
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, -5)

    def test_x_val(self):
        '''
            test value of x
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, -32)

    def test_y_val(self):
        '''
            test value of y
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 5, 32, -64)

    def test_width_zero_val(self):
        '''
            test when width is zero
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(0, 5)

    def test_height_zero_val(self):
        '''
            test when height is zero
        '''
        with self.assertRaises(ValueError):
            r = Rectangle(4, 0)

    def test_x_zero_val(self):
        '''
            test when x is zero
        '''
        self.r = Rectangle(4, 5, 0)
        self.assertEqual(0, self.r.x)

    def test_y_zero_val(self):
        '''
            test when y is zero
        '''
        self.r = Rectangle(4, 5, 32, 0)
        self.assertEqual(0, self.r.y)

    def test_area(self):
        '''
            testing area funtion
        '''
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)
