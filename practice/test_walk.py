import walk_length
import walk_return
import unittest

class Walk(unittest.TestCase):
    def test_walk_exact(self):
        program_input = walk_length.walk_time("neswneswne")
        expected_results = "That was a whole 10 minutes of walking"
        self.assertEqual(program_input, expected_results)
    def test_walk_short(self):
        program_input = walk_length.walk_time("ne")
        expected_results = "You didn't walk long enough"
        self.assertEqual(program_input, expected_results)
    def test_walk_long(self):
        program_input = walk_length.walk_time("neswneswneewsn")
        expected_results = "You walked too long!"
        self.assertEqual(program_input, expected_results)
class Return(unittest.TestCase):
    def test_walk_exact_and_return(self):
        program_input = walk_return.walk_length("neswneswns")
        expected_results = "You came back and made your appointment!"
        self.assertEqual(program_input, expected_results)
    def test_walk_short_and_not_return(self):
        program_input = walk_return.walk_length("ne")
        expected_results = "You did not travel long enough and didn't return to the appointment"
        self.assertEqual(program_input, expected_results)
    def test_walk_long_and_not_return(self):
        program_input = walk_return.walk_length("neswneswneewsn")
        expected_results = "You were gone too long and did not return to your appointment"
        self.assertEqual(program_input, expected_results)
    def test_walk_short_and_return_early(self):
        program_input = walk_return.walk_length("nsew")
        expected_results = "You arrived too early!"
        self.assertEqual(program_input, expected_results)
    def test_walk_long_and_return_late(self):
        program_input = walk_return.walk_length("nsnsewewnsnsewew")
        expected_results = "You came back but were gone too long and missed your appointment!"
        self.assertEqual(program_input, expected_results)
if __name__ == "__main__":
    unittest.main()

