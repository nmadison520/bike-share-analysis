"""Planet attributes established.

This program returns values for different attributes
of the planets in the Solar System. Planets are
characterized according to their planet type and
their habitability.
"""
from math import pi


class Planet:
    """Represents a planet in the Solar System.

    This class is indicative of a planet found in the
    Solar System. It takes note of properties of the
    planet and offers means of classifying the planet.
    """
    def __init__(self, name, mass, radius, distance_from_sun,
                 orbital_period):
        """This method initializes different attributes of the planet.

        The following parameters are defined: name, mass, radius,
        distance_from_sun, and orbital_period.
        """
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance_from_sun = distance_from_sun
        self.orbital_period = orbital_period

    def __str__(self):
        """"It returns a formatted string for this planet."""
        return (f"{self.name}: Mass={self.mass:.2e} kg, Radius={self.radius} km, "
                f"Distance={self.distance_from_sun} million km, "
                f"Orbital Speed={self.calculate_orbital_speed()} km/s, "
                f"Surface Gravity={self.calculate_surface_gravity()} m/s^2")

    def calculate_orbital_speed(self):
        """This method returns the speed of the planet's orbit.

        It is based on how far it is from the sun and how long the
        planet takes to complete one full revolution.
        """
        # Simplified orbital speed formula: v = 2πr / T
        r_km = self.distance_from_sun * 1e6  # convert million km to km
        T_sec = self.orbital_period * 24 * 3600  # convert days to seconds
        speed = (2 * pi * r_km) / T_sec
        return round(speed, 2)


    def calculate_surface_gravity(self):
        """This method calculates the gravity of the planet based on radius.

        It returns the gravity using the formulas below.
        It computes the surface gravity using 2 formulas.
        """
        G = 6.67430e-11  # m^3/kg/s^2
        radius_m = self.radius * 1000  # convert km to meters
        gravity = (G * self.mass) / (radius_m ** 2)
        return round(gravity, 2)  # m/s^2

    def get_info(self):
        """This method returns a dictionary after taking self as a parameter."""
        return {
                "name": self.name,
                "mass": self.mass,
                "radius": self.radius,
                "distance_from_sun": self.distance_from_sun,
                "orbital_period": self.orbital_period,
                "orbital_speed": self.calculate_orbital_speed(),
                "surface_gravity": self.calculate_surface_gravity()
                }

    def planet_type(self) -> str:
        """Classifies planets.

        This method returns either Gas Giant, Terrestrial, or Ice Giant or
        Unknown.
        """
        if self.mass > 1e25 and self.radius > 30000 :
            return "Gas Giant"
        elif self.mass < 1e24 and self.radius < 7000 :
            return "Terrestrial"
        else:
            return "Ice Giant or Unknown"

    def is_habitable(self):
        """Returns True/False.

        This method returns True if the planet type falls
        within the measurements of 'Terrestrial.'
        However, if otherwise, it returns False.
        """
        if self.planet_type() == "Terrestrial":
            return True
        else:
            return False
