#!/usr/bin/python3
import unittest
from models.square import Square
'''
    module to test Square
'''

class TestSquare(unittest.TestCase):
    '''
        class to test Square
    '''

    def test_init(self):
        '''
            test init of square
        '''
        s = Square(5, 32, 64, 89)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 32)
        self.assertEqual(s.y, 64)
        self.assertEqual(s.id, 89)

    def test_str(self):
        '''
            test __str__ method
        '''
        s = Square(5, 32, 64, 89)
        self.assertEqual(str(s), "[Square] (89) 32/64 - 5")

    def test_update(self):
        '''
            test when updated
        '''
        s = Square(5, 32, 64, 89)
        s.update(90, 6, 33, 65)
        self.assertEqual(s.id, 90)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 33)
        self.assertEqual(s.y, 65)
