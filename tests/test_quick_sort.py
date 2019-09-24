import unittest

from src.quicksort import quicksort


class TestQuicksort(unittest.TestCase):
    def test_quicksort_with_ints(self):
        self.assertEqual(quicksort([3, 1, 4, 2, -1]), [-1, 1, 2, 3, 4])

    def test_quicksort_with_strs(self):
        self.assertEqual(quicksort(["a", "j", "e", "z"]), ["a", "e", "j", "z"])

    def test_quicksort_with_non_comparable(self):
        with self.assertRaises(TypeError):
            quicksort([(1, 2), ("a", 3)])
