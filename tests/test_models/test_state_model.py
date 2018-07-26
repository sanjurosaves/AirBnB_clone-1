#!/usr/bin/python3
'''
    Contain tests for the state module.
'''
import unittest
from models.base_model import BaseModel, Base
from models.state import State
import os


class TestState(unittest.TestCase):
    '''
        Test the State class.
    '''

    def test_State_inheritence(self):
        '''
            Test that State class inherits from BaseModel.
        '''
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        '''
            Test that State class contains the attribute `name`.
        '''
        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        '''
            Test that State class attribute name is class type str.
        '''
        new_state = State()
        name = getattr(new_state, "name")
        if name:
            self.assertIsInstance(name, str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "skip unless db")
    def test__Stateinheritence2(self):
        '''
            tests that the State class Inherits from BaseModel
        '''
        new_state = State()
        self.assertIsInstance(new_state, Base)
