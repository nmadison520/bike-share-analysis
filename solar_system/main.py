"""Main for project 2."""

from planet import Planet
from solar_system import SolarSystem
from star import Star


def main():
    """The purpose of the main function is to get user input.

    By using imports from other files, it can produce output
    that is consistent with other information regarding
    the planets. The star and solar system are created,
    and planet objects are used here. The user is asked for input
    tht they'd like to see, andthe distances, planet types, and
    orbital speeds are printed.
    """
    sun = Star("Sun", 1.989e30, "G-type")

    solar_system = SolarSystem("Solar System", sun)

    planets_data = [
        ("Mercury", 3.285e23, 2439.7, 57.9, 87.97),
        ("Venus", 4.867e24, 6051.8, 108.2, 224.70),
        ("Earth", 5.972e24, 6371, 149.6, 365.26),
        ("Mars", 6.39e23, 3389.5, 227.9, 686.98),
        ("Jupiter", 1.898e27, 69911, 778.5, 4332.82),
        ("Saturn", 5.683e26, 58232, 1434, 10755.70),
        ("Uranus", 8.681e25, 25362, 2871, 30687.15),
        ("Neptune", 1.024e26, 24622, 4495, 60190.03)
    ]
    planets = []
    #creates an empty list
    for name, mass, radius, distance, period in planets_data:
        planet = Planet(name, mass, radius, distance, period)
        solar_system.add_planet(planet)
        #add this to the current code so that the planet
        #list can be added and used in the code
        planets.append(planet)

    #1) Distance from Sun
    choice = input("\nDo you want to see distances from the Sun? (yes/no): ")
    if choice == "yes":
        print("\nDistance from Sun (million km):\n")
        for p in planets:
            print(f"{p.name}: {p.distance_from_sun}")
    #2) Planet Types
    choice= input("\nDo you want to see planet types? (yes/no): ")
    if choice== "yes":
        print("\nPlanet Types:\n")
        for p in planets:
            print(f"{p.name} : {p.planet_type()}")
     #3) Orbital Speeds
    choice= input("Do you want to see orbital speeds? (yes/no): ")
    if choice== "yes":
        print("\nOrbital Speeds:\n")
        for p in planets:
            print(f"{p.name} : {p.calculate_orbital_speed():.2f}")
if __name__ == '__main__':
    main()