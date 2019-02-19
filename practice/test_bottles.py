import unittest
import bottles
class testBottles (unittest.TestCase):
    def test_bottle_count_10_gallons_80_percent(self):
        result_bottles_percent= bottles.max_bottle_percent(10, .8)
        expected_bottles_percent = (47.0, 0.8067579787234043)
        self.assertEqual(expected_bottles_percent, result_bottles_percent)

    def test_bottle_count_1_gallon_80_percent(self):
        result_bottles_percent = bottles.max_bottle_percent(1, .8)
        expected_bottles_percent = (4.0, 0.9829406250000001)
        self.assertEqual(expected_bottles_percent, result_bottles_percent)

    def test_bottle_count_100_gallons_90_percent(self):
        result_bottles_percent = bottles.max_bottle_percent(100, .9)
        expected_bottles_percent = (420.0, 0.9014312169312169)
        self.assertEqual(expected_bottles_percent, result_bottles_percent)


if __name__ == '__main__':
    unittest.main()