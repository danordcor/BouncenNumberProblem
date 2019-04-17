import unittest

from bouncy import is_increasing_number, is_decreasing_number, is_bouncy_number, least_bouncy_number_of_proportion


class TestBounceProblem(unittest.TestCase):

    def test_increasing_number(self):
        """Check the method is_increasing_number """
        self.assertTrue(is_increasing_number([1, 3, 4, 4, 6, 8]))
        self.assertFalse(is_increasing_number([6, 6, 4, 2, 0]))

    def test_decreasing_number(self):
        """Check the method is_increasing number """
        self.assertTrue(is_decreasing_number([6, 6, 4, 2, 0]))
        self.assertFalse(is_decreasing_number([1, 3, 4, 4, 6, 8]))

    def test_bouncy_number(self):
        """Check the method is_bouncy_number """
        self.assertTrue(is_bouncy_number(155349))
        self.assertFalse(is_bouncy_number(134468))
        self.assertFalse(is_bouncy_number(66420))

    def test_proportion_of_bouncy_numbers(self):
        """Check the method least_bouncy_number_of_proportion with 50% and 90% """
        self.assertEqual(least_bouncy_number_of_proportion(50), 538)
        self.assertEqual(least_bouncy_number_of_proportion(90), 21780)


if __name__ == '__main__':
    unittest.main()
