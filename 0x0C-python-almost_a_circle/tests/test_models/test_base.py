#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square
import json
import inspect
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

    def test_tuple_id(self):
        '''
            checking when id is tuple
        '''
        b = Base((32,))
        self.assertEqual((32,), b.id)

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

    def test_to_json(self):
        '''
            testing when json
        '''
        s = Square(2)
        json_dict = s.to_dictionary()
        json_str = Base.to_json_string([json_dict])
        self.assertEqual(type(json_str), str)

    def test_json_val(self):
        '''
            testing the json string
        '''
        s = Square(2, 0, 0, 89)
        json_dict = s.to_dictionary()
        json_str = Base.to_json_string([json_dict])
        self.assertEqual(json.loads(json_str),
                        [{"id": 89, "y": 0, "size": 2, "x": 0}])

    def test_json_None(self):
        '''
            testing when None
        '''
        s = Square(2, 0, 0, 89)
        json_dict = s.to_dictionary()
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")

    def test_json_empty(self):
        '''
            testing when empty list passed
        '''
        s = Square(2, 0, 0, 89)
        json_dict = s.to_dictionary()
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")



class TestMethod(unittest.TestCase):
    '''
        class testing methods of Base
    '''

    @classmethod
    def setUpClass(cls):
        '''
            checking doctests
        '''
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_mod_ds(self):
        '''
            test if module docstring documentation exist
        '''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_class_docs(self):
        '''
            test if class docstring doc exist
        '''
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_fun_docs(self):
        '''
            test docstring for function
        '''
        for fun in self.setup:
            self.assertTrue(len(fun[1].__doc__) >= 1)
