from pyjordan.strings import str_replace_all


class TestStrReplace():

    def test_str_replace_all(self):
        x = "The quick brown fox"
        d = {'brown': 'green', 'quick': 'slow', 'fox': 'platypus'}
        self.assertEqual(str_replace_all(x, d), "The slow green platypus")
