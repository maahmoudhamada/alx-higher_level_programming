#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest test suites for max_integer()"""

    def test_emptylist(self):
        """Method to test empty values passed"""
        self.assertEqual(max_integer([]), None)
        self.assertIsNone(max_integer(), None)
        self.assertEqual(max_integer(), None)
        self.assertIsNone(max_integer([]), None)
        self.assertIsNone(max_integer({}), None)

    def test_negative_values(self):
        """Method to test negative values passed"""
        self.assertEqual(max_integer([-4, -1, -23, -11]), -1)
        self.assertEqual(max_integer([-4, -1.5, -23, -11, -1]), -1)

    def test_multiple_types(self):
        """Method to test different data types ex: dict, tuple"""
        self.assertEqual(max_integer([10, 1, 2, 3, 4]), 10)
        self.assertEqual(max_integer([1, 2, 3, 4, 4.1]), 4.1)
        self.assertEqual(max_integer(['A', 'L', 'X']), 'X')
        self.assertEqual(max_integer((1, 5, 3, 4, 5)), 5)
        self.assertEqual(max_integer("ALX"), 'X')

    def test_single_elemnts(self):
        """Method to test a single element passed as a list"""
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer("a"), 'a')

    def test_raises(self):
        """Method to test Exceptions raised"""
        with self.assertRaises(KeyError):
            max_integer({'a': 10, 'b': 5, 'c': 200})
        with self.assertRaises(TypeError):
            max_integer(1)
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3, 4})
