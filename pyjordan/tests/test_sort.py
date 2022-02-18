import unittest
from pyjordan.sort import (
    sort_by
)


class TestStrReplace(unittest.TestCase):

    def test_sort_by(self):
        x = [1, 2, 3, 4, 5]
        y = [9, 8, 7, 0, 1]
        res = sort_by(x, y)
        exp = [4, 5, 3, 2, 1]
        self.assertEqual(res, exp)
