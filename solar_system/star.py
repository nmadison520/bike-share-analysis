"""Creates a star object.

This program is designed to represent and organize
the information surrounding a star object.  That way,
this information can be used in the Solar System
as it requires a central star.
"""

class Star:
    """This class defines a class of type Star.

    It returns a name, mass, and classification type.
    """
    def __init__(self, name: str, mass: float, type: str):
        """A Star is initialized.

        The following 3 arguments- name, mass, and type are passed.
        """
        self.name= name
        self.mass= mass
        self.type= type

    def __str__(self):
        """Defines strings.

        This method uses f strings to return and define the string
        representation of each object.
        """
        return f"Star {self.name}:Type={self.type},Mass={self.mass} kg"
