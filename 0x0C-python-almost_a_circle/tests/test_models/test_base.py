#!/usr/bin/python3
import unittest
from models.base import Base
import json
'''
    defining class test_base
'''


class test_base(unittest.TestCase):
    '''
        class to test base module
    '''

    def test_id_none(self):
        '''
            if id is none
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id_not_none(self):
        ''' 
            class to check id
        '''
        b = Base(89)
        self.assertEqual(89, b.id)
