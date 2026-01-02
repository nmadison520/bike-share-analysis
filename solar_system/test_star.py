"""Unit tests for the Star class from the star_soln module."""

import unittest

from star import Star


class TestStar(unittest.TestCase):
    """Testing the Star class."""
    def setUp(self):
        """Create a Star instance for use in all test methods."""
        self.star = Star("Proxima Centauri", 0.122, ' M-type')

    # test the __str__ method
    def test_str(self):
        """This method returns the string formatted."""
        expected_value = "Star Proxima Centauri: Type= M-Type, Mass= 0.122 kg"
        self.assertEqual(str(self.star), expected_value)

if __name__ == '__main__':
    unittest.main(verbosity=2)
