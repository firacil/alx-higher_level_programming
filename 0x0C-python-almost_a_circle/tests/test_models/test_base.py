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
            check id
        '''
        b = Base(89)
        self.assertEqual(89, b.id)

    def test_id_list(self):
        '''
            checking when id is list
        '''
        b = Base([1, 2])
        self.assertEqual([1, 2], b.id)

    def test_check_dic(self):
        '''
            checking when id is dict
        '''
        b = Base({"id": 53})
        self.assertEqual({"id": 53}, b.id)

    def test_id_zero(self):
        '''
            checking when id is zero
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_neg(self):
        '''
            when id is negative
        '''
        b = Base(-23)
        self.assertEqual(-23, b.id)
