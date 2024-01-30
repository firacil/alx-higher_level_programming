#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests whether module prints maximum integer or nuo"""
    def outp(self):
        self.list = [1, 2, 3, 4]


if __name__ == '__main__':
    unittest.main()
