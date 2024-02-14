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
        self.r = Rectangle(4, 5)

    def test_teardown(self):
        '''
            delete created instances
        '''
        del self.r

    def test_width(self):
        '''
            testing rectangles width getter
        '''
        self.assertEqual(4, self.r.width)

    def test_height(self):
        '''
            testing rectangles height getter
        '''
        self.assertEqual(5, self.r.height)

    def test_attr(self):
        '''
            testing attributes of rectangle
        '''
        rectangle = Rectangle(5, 10, 1, 2, 100)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 100)

    def test_area(self):
        '''
            testing area funtion
        '''
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)
