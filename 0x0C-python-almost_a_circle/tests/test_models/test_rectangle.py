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

    def test_area(self):
        '''
            testing area funtion
        '''
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)
