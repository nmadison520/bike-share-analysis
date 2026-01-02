"""Main file to run the volcano monitoring system."""

from sensor import Sensor
from volcano import Volcano
from warning import Warning


def main():
    """Main function to run the volcano monitoring simulation.

    Creates sensors, a volcano, and a warning system,
      then prints the status and warning.
    """
    # Create sensors
    pressure = Sensor("pressure", 600)
    temperature = Sensor("temperature", 850)
    seismic = Sensor("seismic", 8)

    # Create volcano
    volcano = Volcano("Mount Sassmore", pressure, temperature, seismic)

    # Create warning system
    styles = ['sassy', 'poetic', 'scientific']
    for styl in styles:
        print(styl)
        warning_system = Warning(style=styl)

        # Run simulation
        status = volcano.check_status()
        message = warning_system.generate(volcano.name, status)

        print(message)
        print(volcano.name + " status:", status)
        print()


if __name__ == "__main__":
    main()
