"""Unit Test for the Planet Class."""

import unittest

from planet import Planet


class TestPlanet(unittest.TestCase):
    """Testing Planet Class."""
    def setUp(self):
        """Creating default Planet Object.

        Remember setUp() will run before each test method.
        """
        self.planet = Planet("Mars", 1.41e25, 2718.3, 271828.18, 789)

    def test_str(self):
        """Tests str for expected values.

        Testing the representation of the Planet object.
        """
        expected_value = "Mars: Mass=1.41e+25 kg, Radius=2718.3 km, "
        "Distance=271828.18 million km, "
        "Orbital Speed=25054.38 km/s, "
        "Surface Gravity=127.36 m/s^2"
        result = str(self.planet)
        self.assertEqual(result, expected_value)

    def test_get_get_info(self):
        """Test for the expected keys.

        This program returns a dictionary with the correct keys and
        values.
        """
        info= self.planet.get_info()
        expected_keys= {
            "name",
            "mass",
            "radius",
            "distance_from_sun",
            "orbital_period",
            "orbital_speed",
            "surface_gravity"
        }
        self.assertEqual(set(info.keys()), expected_keys)

        self.assertEqual(info["name"], "Mars")
        self.assertEqual(info["mass"], 1.41e25)
        self.assertEqual(info["radius"], 2718.3)
        self.assertEqual(info["distance_from_sun"], 271828.18)
        self.assertEqual(info["orbital_period"], 789)

        #orbital_speed and surface_gravity given above
        self.assertEqual(info["orbital_speed"], 25054.38)
        self.assertEqual(info["surface_gravity"], 127.36)

    def test_calculate_orbital_speed(self):
        """Test for orbital speed.

        This test will check to see if it returns the expected 2 decimal
        value given for orbital_speed.
        """
        self.assertEqual(self.planet.calculate_orbital_speed(), 25054.38)

    def test_calculate_surface_gravity(self):
        """Test for surface gravity.

        This test will check to see if it returns the expected 2
        decimal value for the given surface gravity.
        """
        self.assertEqual(self.planet.calculate_surface_gravity(), 127.36)

    def test_planet_type_terrestrial(self):
        """Tests for terrestrial.

        This test checks to see if the planet's values
        fit within the parameters of the 'terrestrial'
        planet type.
        """
        p = Planet("Rock1", 1.4e21, 5500, 12.0, 150)
        self.assertEqual(p.planet_type(), "Terrestrial")

    def test_planet_type_gas_giant(self):
        """Tests for gas giant.

        This test checks to see if the planet's values
        fit within the parameters of the 'gas giant'
        planet type.
        """
        p = Planet("Rock2", 1.0e26, 35000, 150.0, 6500)
        self.assertEqual(p.planet_type(), "Gas Giant")

    def test_planet_type_else_unknown(self):
        """Tests for uknown type.

        This test checks to see if the planet's values
        fit within the parameters of the 'else or unknown'
        planet type since it does not fit into the other
        parameters.
        """
        p = Planet("RockUnsure", 6.0e24, 12000, 110.0, 3000)
        self.assertEqual(p.planet_type(), "Ice Giant or Unknown")

        #have to test for the boundaries between those values,
        #because there is no equal to in the equation

    def test_planet_type_boundaries(self):
        """Tests the boundaries.

        This test checks the values at the boundaries
        between gas giant and terrestrial, because there
        is not an equal to option in the current code.
        """
        boundary1 = Planet("Boundary1", 1.0e25, 3000, 1.2, 1)
        self.assertEqual(boundary1.planet_type(), "Ice Giant or Unknown")

        boundary2 = Planet("Boundary2", 1.0e24, 7000, 1.2, 1)
        self.assertEqual(boundary2.planet_type(), "Ice Giant or Unknown")

    def test_is_habitable_true(self):
        """Tests for habitability.

        This test checks to see if the planet
        fits within the parameters that deem
        it to be habitable- this is only when the
        planet is terrestrial.
        """
        p = Planet("SafeforLife", 1e22, 6500, 175.0, 325)
        self.assertTrue(p.is_habitable())

    def test_is_habitable_false(self):
        """Tests for inhabitability.

        This test checks to see if the planet fits
        within the parameters that deem it to be
        uninhabitable- this is true when the planet
        is not terrestrial.
        """
        p1 = Planet("GassyGiant", 2.0e26, 40000, 465.0, 4000)
        p2 = Planet("IcyGiantUnknown", 2.5e24, 20000, 315.0, 2200)
        self.assertFalse(p1.is_habitable())
        self.assertFalse(p2.is_habitable())

if __name__ == '__main__':
    unittest.main(verbosity=2)
