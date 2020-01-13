#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-2, 5, -8, 3]), 5)
        self.assertEqual(max_integer([1]), 1)

    def test_max_list_of_list(self):
        self.assertEqual(max_integer([[5, 6, 8], [1, 2, 4]]), [5, 6, 8])

    def test_max_float(self):
        self.assertEqual(max_integer([5.6, 6, 8.9, 8.5]), 8.9)

    def test_max_empty(self):
        self.assertEqual(max_integer(), None)

    def test_max_instance(self):    
        self.assertNotIsInstance(max_integer([5, 9.2]), int)

    def test_raising(self):
        matrix = [1, 9, 6]
        self.assertEqual(max_integer(matrix), 9)
        with self.assertRaises(TypeError):
            max_integer(['zaco', 'guest', 9])
