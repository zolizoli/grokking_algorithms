import unittest

from src.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search_element_in_lst(self):
        self.assertEqual(binary_search([1, 2, 3], 2), 1)

    def test_binary_search_element_not_in_lst(self):
        self.assertEqual(binary_search([1, 2, 3], 4), -1)

    def test_binary_search_wrong_input_lst(self):
        with self.assertRaises(AssertionError):
            binary_search(["a", "b", "c"], 2)

    def test_binary_search_with_wrong_input_search(self):
        with self.assertRaises(AssertionError):
            binary_search([1, 2, 3], "a")
