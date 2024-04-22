#!/usr/bin/python3
"""The test_base Module
class:
    BaseClassTest()
Methods:
    setupClass: To create instances for test environment
    test_instances: Test subclass
    test_ids: Test ids
    test_nb_objects: Test numbers of objects created
"""


import unittest
from models.base import Base


class BaseClassTest(unittest.TestCase):
    """SubClass of unittest.TestCase Class"""

    @classmethod
    def setUpClass(self):
        """Creating 3 instances of Base class"""
        self.b1 = Base(98)
        self.b2 = Base()
        self.b3 = Base()

    def test_instances(self):
        """Testing if instances created is subclass/inherted from Base class"""
        self.assertIsInstance(self.b1, Base)
        self.assertIsInstance(self.b2, Base)
        self.assertIsInstance(self.b3, Base)

    def test_ids(self):
        """Testing ids if none == nb_objects otherwise == id"""
        self.assertEqual(self.b1.id, 98)
        self.assertEqual(self.b2.id, 1)
        self.assertEqual(self.b3.id, 2)

    def test_nb_objects(self):
        """Testing for number of nb_objects"""
        self.assertEqual(Base._Base__nb_objects, 2)
        self.assertEqual(self.b2.id, 1)
        self.assertEqual(self.b3.id, Base._Base__nb_objects)
