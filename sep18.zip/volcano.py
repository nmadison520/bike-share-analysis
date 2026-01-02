
"""The Volcano Class is used to represent a volcano in the monitoring system."""
#from sensor import Sensor


class Volcano:
    """Represents a volcano with sensors for monitoring eruption conditions.

    Attributes:
        name (str): The name of the volcano.
        pressure_sensor (Sensor): Sensor monitoring pressure.
        temp_sensor (Sensor): Sensor monitoring temperature.
        seismic_sensor (Sensor): Sensor monitoring seismic activity.
    """
    def __init__(self, name, pressure_sensor, temp_sensor, seismic_sensor):
        """Initializes the volcano with its name and associated sensors."""
        self.name = name
        self.pressure_sensor = pressure_sensor
        self.temp_sensor = temp_sensor
        self.seismic_sensor = seismic_sensor

    def __str__(self):
        """Represented by Name: (pressure, temp, seismic)"""
        msg = f"{self.name}: ({self.pressure_sensor.get_reading()}, "
        msg += f"{self.temp_sensor.get_reading()}, "
        msg += f"{self.seismic_sensor.get_reading()})"
        return msg

    def check_status(self):
        """Checks the volcano's status based on sensor readings.

        Returns:
            str: 'eruption imminent' if thresholds are exceeded, otherwise 'stable'.
        """
        pressure = self.pressure_sensor.get_reading()
        temp = self.temp_sensor.get_reading()
        seismic = self.seismic_sensor.get_reading()

        if pressure > 500 and temp > 800 and seismic > 7:
            return "eruption imminent"
        return "stable"
