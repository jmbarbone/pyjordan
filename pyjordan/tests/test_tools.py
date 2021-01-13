from pyjordan.tools import round_by


class TestRoundBy():

    def test_round_by(self):
        x = [1, 2, 3, 4, 5]
        result_r = round_by(x, 2, "round")
        result_f = round_by(x, 2, "floor")
        result_c = round_by(x, 2, "ceiling")
        self.assertEqual(result_r, [0, 2, 4, 4, 4])
        self.assertEqual(result_f, [2, 2, 4, 4, 6])
        self.assertEqual(result_c, [0, 2, 2, 4, 4])
