import unittest
from pyjordan.strings import str_replace_all,  paste_combine


class TestStrReplace(unittest.TestCase):

    def test_str_replace_all(self):
        x = "The quick brown fox"
        d = {'brown': 'green', 'quick': 'slow', 'fox': 'platypus'}
        self.assertEqual(str_replace_all(x, d), "The slow green platypus")


class TestPasteCombine(unittest.TestCase):

    def test_paste_combine(self):
        x = ["a", "b"]
        y = [1, 2]
        z = ["!", "?", "."]
        res1 = ["a1", "a2", "b1", "b2"]
        res2 = ["a_1", "a_2", "b_1", "b_2"]
        res3 = ["a1", "b1", "a2", "b2"]
        res4 = ["a1!", "a1?", "a1.",
                "a2!", "a2?", "a2.",
                "b1!", "b1?", "b1.",
                "b2!", "b2?", "b2."]
        self.assertEqual(paste_combine([x, y]), res1)
        self.assertEqual(paste_combine([x, y], sep="_"), res2)
        self.assertEqual(paste_combine([x, y], collate=False), res3)
        self.assertEqual(paste_combine([x, y, z]), res4)
