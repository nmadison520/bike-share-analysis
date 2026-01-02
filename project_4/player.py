"""Player class for Project 4."""
from participant import Participant


class Player(Participant):
    """Player class is subclass of Participant.

    Player information stores and tournament stats are provided.
    """

    def __init__(self, name, number, school, status="healthy", position=None):
        """Initialize a Player (name, number, school, status, position)."""
        self.name=name
        self.status=status
        self.school=school
        self.number=number
        self.position=position
        self.game_stats={
            "points": 0,
            "rebounds": 0,
            "turnovers": 0,
            "ppg": 0.0
        }
        self.tournament_stats={
            "points": 0,
            "rebounds": 0,
            "turnovers": 0,
            "wins": 0,
            "losses": 0,
            "number_of_games": 0,
            "ppg": 0
        }

    def __eq__(self, other):
        """Compare two player objects.
        This will return T if two player objects equate to each other when
        their attributes including name, school, number attributes are equal.
        """
        if isinstance(other, Player):
            return (self.name== other.name and
                    self.number== other.number and
                    self.school== other.school)
        return False

    def get_tournament_stats(self):
        """Make copy of stats from tournament attribute.

        Add points per game to the copy (ppg).
        Rounds to two decimal places, and returns copy of
        tournament stats as a dict.
        """
        stats_copy={}
        for key in self.tournament_stats:
            stats_copy[key]= self.tournament_stats[key]

        total_points= stats_copy.get("points", 0)
        total_games= stats_copy.get("number_of_games", 0)

        if total_games==0:
            ppg=0.0
        else:
            ppg=int((total_points/total_games)*100)/100.0

        stats_copy["ppg"]= ppg
        return stats_copy

