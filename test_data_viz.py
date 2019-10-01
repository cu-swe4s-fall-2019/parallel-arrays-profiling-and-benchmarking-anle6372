"""Unittesting framework for data_viz.py

Parameters
----------
None

Returns
-------
None
"""

import unittest
import data_viz
import os


# Testing none input
class TestNone(unittest.TestCase):

    def test_boxplot_none(self):
        self.assertEqual(data_viz.boxplot(None, None), None)

    def test_histogram_none(self):
        self.assertEqual(data_viz.histogram(None, None), None)

    def test_combo_none(self):
        self.assertEqual(data_viz.histogram(None, None), None)


# Testing null input
class TestNull(unittest.TestCase):

    def test_boxplot_null(self):
        self.assertRaises(TypeError, lambda: data_viz.boxplot())

    def test_histogram_null(self):
        self.assertRaises(TypeError, lambda: data_viz.histogram())

    def test_combo_null(self):
        self.assertRaises(TypeError, lambda: data_viz.combo())


# Testing incorrect input types
class TestIncorrectInput(unittest.TestCase):

    def setUp(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_boxplot_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(str('hi'),
                                                   self.test_file_name))

    def test_histogram_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(str('hi'),
                                                     self.test_file_name))

    def test_combo_string(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(str('hi'),
                                                 self.test_file_name))

    def test_boxplot_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(4,
                                                   self.test_file_name))

    def test_histogram_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(4, self.test_file_name))

    def test_combo_int(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(4, self.test_file_name))

    def test_boxplot_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(420.69,
                                                   self.test_file_name))

    def test_histogram_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(420.69,
                                                     self.test_file_name))

    def test_combo_float(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(420.69,
                                                 self.test_file_name))

    def test_boxplot_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.boxplot(True,
                                                   self.test_file_name))

    def test_histogram_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.histogram(True,
                                                     self.test_file_name))

    def test_combo_Boolean(self):
        self.assertRaises(TypeError,
                          lambda: data_viz.combo(True,
                                                 self.test_file_name))


# Testing empty list input
class TestEmptyListInput(unittest.TestCase):

    def setUp(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_boxplot_empty_array(self):
        self.assertEqual(data_viz.boxplot([], self.test_file_name), None)

    def test_histogram_empty_array(self):
        self.assertEqual(data_viz.histogram([], self.test_file_name), None)

    def test_combo_empty_array(self):
        self.assertEqual(data_viz.combo([], self.test_file_name), None)


# Testing invalid list input
class TestInvalidListInput(unittest.TestCase):

    def setUp(self):
        self.test_file_name = 'setup_test_file.txt'
        f = open(self.test_file_name, 'w')
        f.close()

    def tearDown(self):
        os.remove(self.test_file_name)

    def test_boxplot_letter_array(self):
        self.assertRaises(ValueError, lambda: data_viz.boxplot(
            ['A', 'B', 'C'], self.test_file_name))

    def test_histogram_letter_array(self):

        self.assertRaises(ValueError, lambda: data_viz.histogram(
            ['A', 'B', 'C'], self.test_file_name))

    def test_combo_letter_array(self):

        self.assertRaises(ValueError, lambda: data_viz.combo(
            ['A', 'B', 'C'], self.test_file_name))


# Testing no file creation
class TestFileNonExistance(unittest.TestCase):

    def test_file_does_not_exist(self):

        self.assertFalse(os.path.exists('test_file_name.png'))


# Testing file creation
class TestFileExistance(unittest.TestCase):
    def setUp(self):
        data_viz.histogram([1], 'test_file_name1.png')
        data_viz.boxplot([1], 'test_file_name2.png')
        data_viz.combo([1], 'test_file_name3.png')

    def test_file_exists(self):

        self.assertTrue(os.path.exists('test_file_name1.png'))

        self.assertTrue(os.path.exists('test_file_name2.png'))

        self.assertTrue(os.path.exists('test_file_name3.png'))


if __name__ == '__main__':
    unittest.main()
