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
        self.assertEqual(max_integer([5.6, 6, 8.9, 8.5]), 8.9)
        self.assertEqual(max_integer([[5, 6, 8], [1, 2, 4]]), [5, 6, 8])
        self.assertEqual(max_integer(), None)

    with self.assertRaises(TypeError):
        max_integer(['zaco', 'guest', 6])
