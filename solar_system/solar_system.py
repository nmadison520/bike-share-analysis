"""This is a model of the Solar System.

In this program, a SolarSystem class is defined.
It initilaizes a star that is central to the
planets themselves.
"""


class SolarSystem:
    """Solar system class is defined.

    In this class, a number of different planets
    orbit a star centralized to the area.
    """
    def __init__(self, new_name, new_star):
        """Initializes solar system.

        In this method, a solar system is initialized, with
        the attributes new_name and new_star. An
        empty set is created to store Planet objects in the
        provided set() function.
        """
        self.name: str = new_name
        self.star: str = new_star
        self.planets: set = set()

    def __str__(self):
        """Returns a string.

        This method returns the string conversion of the
        Solar System and the planets within it.
        """
        result = f'{self.name}:\n  {self.star}\n'
        for planet in self.planets:
            result += (f"  {planet.name}: Mass={planet.mass:.2e} kg, "
                    f"Radius={planet.radius} km, "
                    f"Distance={planet.distance_from_sun} million km, "
                    f"Orbital Speed={planet.calculate_orbital_speed()} km/s "
                    f"Surface Gravity={planet.calculate_surface_gravity()}  m/s^2\n\n")
        return result

    def list_planets(self):
        """"Returns a list.

        This method returns a list of all of the planet
        names in the Solar System.
        """
        return [planet.name for planet in self.planets]

    def add_planet(self, planet):
        """Returns True/False.

        This method takes self and the planet
        object as parameters and returns a Boolean.
        It will return True if the planet was added
        successfuly, and False if otherwise.
        """
        if planet in self.planets:
            return False
        self.planets.add(planet)
        return True

    def find_habitable_planets(self):
        """Returns planets.

        This method returns all planets that
        are considered to be habitable- including the
        name of the planet and whether it is habitable.
        """
        return [planet.name for planet in self.planets if planet.is_habitable()]
