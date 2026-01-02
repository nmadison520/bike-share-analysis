"""Volcano Test Class using unittest."""

import unittest

from sensor import Sensor
from volcano import Volcano


class TestVolcano(unittest.TestCase):
    """Defining the TestVolcano Class."""
    def setUp(self):
        """Defining the default vars and values.

        Remember this is run before each test class.
        """
        self.pressure = Sensor("pressure", 300)
        self.temperature = Sensor("temperature", 350)
        self.seismic = Sensor("seismic", 5)
        self.volcano = Volcano("Serious", 
                               self.pressure,
                               self.temperature,
                               self.seismic
                               )
        
    def test_str(self):
        """Making sure the representation is correctly displayed."""
        result = str(self.volcano)
        expected_value = "Serious: (300, 350, 5)"
        self.assertEqual(result, expected_value)

    def test_check_status_ttt(self):
        """Checking when check_status returns eruption imminent"""
        self.pressure.update(501)
        self.temperature.update(801)
        self.seismic.update(7.000001)
        result = self.volcano.check_status()
        expected_value = "eruption imminent"
        self.assertEqual(result, expected_value)
    
    def test_check_status_ttt(self):
        """Checking when check_status returns eruption imminent"""
        self.pressure.update(501)
        self.temperature.update(801)
        self.seismic.update(7)
        result = self.volcano.check_status()
        expected_value = "stable"
        self.assertEqual(result, expected_value)
    
    def test_check_status_ttt(self):
        """Checking when check_status returns eruption imminent"""
        self.pressure.update(501)
        self.temperature.update(800)
        self.seismic.update(10)
        result = self.volcano.check_status()
        expected_value = "stable"
        self.assertEqual(result, expected_value)

    def test_check_status_f(self):
        """Checking when check_status returns stable"""
        result = self.volcano.check_status()
        expected_value = "stable"
        self.assertEqual(result, expected_value)

if __name__ == '__main__':
    unittest.main(verbosity=2)