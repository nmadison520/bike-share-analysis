"""Sensor Class using unittest."""

import unittest

from sensor import Sensor


class TestSensor(unittest.TestCase):
    """Defining the TestSenor Class."""
    def setUp(self):
        """Defining the default vars and values.

        Remember this is run before each test class.
        """
        self.sensor = Sensor("pressure", 500)

    def test_str(self):
        """Let's make sure the representation is correct."""
        result = str(self.sensor)
        expected_value = "Sensor(type = pressure, reading = 500)"
        self.assertEqual(result, expected_value)

    def test_update_and_get(self):
        """Update reading to 600 and test."""
        self.sensor.update(600)
        result = self.sensor.get_reading()
        expected_value = 600
        self.assertEqual(result, expected_value)

if __name__ == "__main__":
    unittest.main(verbosity=2)
