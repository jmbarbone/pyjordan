import unittest
from pyjordan.tools import round_by, unnest


class TestRoundBy(unittest.TestCase):

    def test_round_by(self):
        x = [1, 2, 3, 4, 5]
        result_r = round_by(x, 2, "round")
        result_f = round_by(x, 2, "floor")
        result_c = round_by(x, 2, "ceiling")
        self.assertEqual(result_r, [0, 2, 4, 4, 4])
        self.assertEqual(result_f, [0, 2, 2, 4, 4])
        self.assertEqual(result_c, [2, 2, 4, 4, 6])


class TestUnnest(unittest.TestCase):
    def test_unnest(self):
        x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        y = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(unnest(x), y)

        x = [1, [2, 3], 4, 5, [6, 7, 8, 9]]
        self.assertEqual(unnest(x), y)

        x = ["a", "b", ["c", "d"]]
        y = ["a", "b", "c", "d"]
        self.assertEqual(unnest(x), y)

        # Multiple imbedded lists
        self.assertEqual(unnest([[1], [2, [3, 4]]]), [1, 2, 3, 4])
