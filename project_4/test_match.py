"""Test for match."""
import unittest

from match import Match
from team import Team


class TestMatch(unittest.TestCase):
    """Unit test for Match class."""

    def setUp(self):
        """Set up test case with test names."""
        self.team1=Team("Rutgers")
        self.team2=Team("Monmouth")
        self.team3=Team("Princeton")
        self.match1=Match(1, self.team1, self.team2, status="scheduled")

    def test_str_(self):
        """Test that str returns correct string."""
        self.assertEqual(str(self.match1), "1: scheduled")
    def test_eq_match(self):
        """Test that two matches are actually equal."""
        other= Match(1, Team("Rutgers"), Team("Monmouth"))
        self.assertTrue(self.match1==other)
    def test_eq_if_swapped(self):
        """Test that matches are equal even if order is changed."""
        other=Match(1, Team("Monmouth"), Team("Rutgers"))
        self.assertTrue(self.match1==other)
    def test_eq_diff(self):
        """Test that matches with unequal ids are not equal."""
        other=Match(2, Team("Rutgers"), Team("Monmouth"))
        self.assertFalse(self.match1==other)
    def test_diff_teams(self):
        """Test that matches with different teams are unequal."""
        other=Match(1, Team("Rutgers"), Team("Princeton"))
        self.assertFalse(self.match1==other)

if __name__ == "__main__":
    unittest.main(verbosity=2)
