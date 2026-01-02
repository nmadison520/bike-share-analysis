"""This program tests the solar system progeam.

It ensures that the solar system class and its
functions by representing them as strings work
as they should be.
"""

import unittest

from planet import Planet
from solar_system import SolarSystem


class TestSolar(unittest.TestCase):
    """This tests for the Solar System class."""

    def setUp(self):
        """Initializing a Solar System object.

        Remember that setUP() is run before each test method.
        """
        self.solar_sys = SolarSystem("Zed", "Zamp")

    def test__str(self):
        """Verifies that the string representation of a SolarSystem object."""
        p = Planet("P", 1, 1, 1, 1)
        self.solar_sys.add_planet(p)
        expected_value = "Zed:\n  Zamp\n  "
        expected_value += "P: Mass=1.00e+00 kg, Radius=1 km, Distance=1 million km, "
        "Orbital Speed=72.72 km/s Surface Gravity=0.0  m/s^2\n\n"
        self.assertEqual(str(self.solar_sys), expected_value)

    def test_list_planets(self):
        """Verifies when the list is empty and has 1 element."""
        result = self.solar_sys.list_planets()
        self.assertEqual(len(result), 0)
        z_planet = Planet("z", 1, 2, 3, 4)
        self.solar_sys.add_planet(z_planet)
        result = self.solar_sys.list_planets()
        self.assertEqual(result, ['z'])


if __name__ == '__main__':
    unittest.main(verbosity=2)
