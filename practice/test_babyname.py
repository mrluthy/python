import babyname
import unittest
import string
from random import Random

random = Random()

class names(unittest.TestCase):
    def test_babyname1(self):
        letter_input_1 = 'c'
        letter_input_2 = 'v'
        letter_input_3 = 'l'
        letter_input_4 = 'v'
        letter_input_5 = 'c'
        result = babyname.generator()
        expected = random.choice('bcdfgh')
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()