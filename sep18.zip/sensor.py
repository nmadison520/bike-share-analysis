
"""The Sensor class is used in volcanic monitoring systems."""

class Sensor:
    """Represents a sensor that monitors a specific type of volcanic data.

    Attributes:
        sensor_type (str):
          The type of sensor (e.g., 'pressure', 'temperature', 'seismic').
        reading (float): The current reading from the sensor.
    """
    def __init__(self, sensor_type, reading):
        """Initializes the sensor with a type and initial reading."""
        self.sensor_type = sensor_type
        self.reading = reading

    def __str__(self):
        """Returning sensor type and reading in a readable format."""
        return f"Sensor(type = '{self.sensor_type}', reading = {self.reading})"

    def update(self, new_reading):
        """Updates the sensor's reading.

        Args:
            new_reading (float): The new value to set for the sensor.
        """
        self.reading = new_reading

    def get_reading(self): 
        """Returns the current reading of the sensor.

        Returns:
            float: The current sensor reading.
        """
        return self.reading
