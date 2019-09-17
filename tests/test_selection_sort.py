import unittest

from src.selection_sort import findSmallest, selectionSort


class TestSelectionSort(unittest.TestCase):
    def test_findSmallest_ints(self):
        self.assertEqual(findSmallest([1,2,3]), 0)

    def test_findSmallest_not_ints(self):
        with self.assertRaises(AssertionError):
            findSmallest(["a", "c", "d"])

    def test_selectionSort_with_ints(self):
        self.assertEqual(selectionSort([3, 1, 4, 2, -1]), [-1, 1, 2, 3, 4])

    def test_selectionSort_with_not_ints(self):
        with self.assertRaises(AssertionError):
            selectionSort(["a", "b", "d"])
