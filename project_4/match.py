"""Match class definition for tournament."""
class Match:
    """Represent single contest between two participants."""

    def __init__(self, id,  team1, team2, status="not started"):
        """Initialize match object."""
        self.id= id
        self.bracket_id=None
        self.team1= team1
        self.team2= team2
        self.status= status
        self.score= (0,0)

    def __str__(self):
        """Return string showing match id and status of such.

        Returns string in template of id: status.
        """
        return f"{self.id}: {self.status}"

    def __eq__(self, other):
        """Check for match object equality- returns True if both match
        objecrs are equal when ids and teams are equal, otherwise false.
        """
        if isinstance(other, Match):
            return (
                self.id==other.id and
                (
                (self.team1==other.team1 and self.team2==other.team2)
                or
                (self.team1==other.team2 and self.team2==other.team1)
                )
            )
        return False
