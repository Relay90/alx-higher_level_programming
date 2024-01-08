#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from my_module import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_duplicate_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)
        self.assertEqual(max_integer([0, 0, 0]), 0)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)
        self.assertEqual(max_integer([-10, 10, 5]), 10)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1000000, 999999, 10000000]), 10000000)

if __name__ == '__main__':
    unittest.main()
