#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest


class RectangleClassTest(unittest.TestCase):
    """"""
    
    @classmethod
    def setUpClass(self):
        self.r1 = Rectangle(2, 3, 1, 1, 98)
        self.r2 = Rectangle(4, 5, 2, 2)
        self.r3 = Rectangle(10, 10, 10, 10, 98)
        self.r4 = Rectangle(2, 2, 2, 2, 12)

    @classmethod
    def tearDownClass(self):
        del self.r1
        del self.r2
        del self.r3

    # ==========================  test_instances  =======================

    def test_instances(self):
        self.assertIsInstance(self.r1, Rectangle)
        self.assertIsInstance(self.r2, Rectangle)

    # ==========================  test_ids  ============================

    def test_ids(self):
        self.assertEqual(self.r1.id, 98)
        self.assertEqual(self.r2.id, Rectangle._Base__nb_objects)
        self.assertEqual(self.r2.id, 3)

    # ==========================  test_width  ============================

    def test_width(self):
        self.assertEqual(self.r1.width, 2) # test width.getter
        self.r1.width = 7
        self.assertEqual(self.r1.width, 7) # test width.setter
        with self.assertRaises(TypeError): # test Non-integer values
            self.r1.width = '7'
        with self.assertRaises(ValueError): # test Zero value
            self.r2.width = 0
        with self.assertRaises(ValueError): # test Negative values
            self.r2.width = -10

    # ==========================  test_height  ============================

    def test_height(self):
        self.assertEqual(self.r1.height, 3) # test height.getter
        self.r1.height = 7
        self.assertEqual(self.r1.height, 7) # test height.setter
        with self.assertRaises(TypeError): # test Non-integer values
            self.r1.height = '7'
        with self.assertRaises(ValueError): # test Zero value
            self.r2.height = 0
        with self.assertRaises(ValueError): # test Negative values
            self.r2.height = -10
            
    # ==========================  test_x  ============================

    def test_x(self):
        self.assertEqual(self.r1.x, 1) # test x.getter
        self.r1.x = 7
        self.assertEqual(self.r1.x, 7) # test x.setter
        with self.assertRaises(TypeError): # test Non-integer values
            self.r1.x = '7'
        with self.assertRaises(ValueError): # test Negative values
            self.r2.x = -10

    # ==========================  test_y  ============================

    def test_y(self):
        self.assertEqual(self.r1.y, 1) # test y.getter
        self.r1.y = 7
        self.assertEqual(self.r1.x, 7) # test y.setter
        with self.assertRaises(TypeError): # test Non-integer values
            self.r1.y = '7'
        with self.assertRaises(ValueError): # test Negative values
            self.r2.y = -10

    # ==========================  test_str  ============================

    def test_str(self):
        self.assertEqual(str(self.r3), '[Rectangle] (98) 10/10 - 10/10')

    # ==========================  test_area  ============================

    def test_area(self):
        self.assertEqual(self.r3.area(), 100)

    # ==========================  test_display  ============================
    
    def test_display(self):
        self.assertEqual(self.r4.display(), None)

