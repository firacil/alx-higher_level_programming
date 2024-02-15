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

    def test_to_dictionary(self):
        '''
            testing method to dictionary
        '''
        s = Square(5, 32, 64, 89)
        sq_dict = s.to_dictionary()
        ex_dict = {'id': 89, 'size': 5, 'x': 32, 'y': 64}
        self.assertEqual(sq_dict, ex_dict)

    def test_size_type(self):
        '''
            testing TypeError
        '''
        with self.assertRaises(TypeError):
            s = Square("testing")

    def test_size_value(self):
        '''
            testing when unwanted value occured
        '''
        with self.assertRaises(ValueError):
            s = Square(-5)

    def test_size_zero(self):
        '''
            testing when size passed as zero
        '''
        with self.assertRaises(ValueError):
            s = Square(0)
