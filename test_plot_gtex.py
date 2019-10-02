"""Unittesting framework for plot_gtex.py

Parameters
----------
None

Returns
-------
None
"""

import unittest
import plot_gtex
import random


# Testing none input
class TestNone(unittest.TestCase):

    def test_plot_gtex_none(self):
        self.assertEqual(plot_gtex.linear_search(None, None), None)


# Testing incorrect input
class TestIncorrect(unittest.TestCase):
    def test_plot_gtex_string(self):
        self.assertRaises(TypeError,
                          lambda: plot_gtex.linear_search(str('key'), str('hi')))

    def test_plot_gtex_int(self):
        self.assertRaises(TypeError,
                          lambda: plot_gtex.linear_search(str('key'), 4))

    def test_plot_gtex_bool(self):
        self.assertRaises(TypeError,
                          lambda: plot_gtex.linear_search(str('key'), True))

    def test_plot_gtex_float(self):
        self.assertRaises(TypeError,
                          lambda: plot_gtex.linear_search(str('key'), float(4)))

# Testing mixed types
class TestMixedTypes(unittest.TestCase):
    def test_plot_gtex_string_int(self):
        self.assertRaises(TypeError,
                          lambda: plot_gtex.linear_search(str('key'), [1, 2, 3, 4, 5, 6, 7, 8]))

# Testing correct input
class TestCorrectConstant(unittest.TestCase):

    def test_plot_gtex_const_int(self):
        self.assertEqual(plot_gtex.linear_search(4, [1, 2, 3, 4, 5, 6, 7, 8]), 3)

    def test_plot_gtex_const_str(self):
        self.assertEqual(plot_gtex.linear_search(str('cat'), [str('dog'), str('cat'), str('walrus')]), 1)


if __name__ == '__main__':
    unittest.main()