"""Team for Project 4."""
from participant import Participant


class Team(Participant):
    """Team class is a subclass of Participant.

    Player objects roster is held and tournament stats including wins/losses.
    """

    def __init__(self, school_name, status= "active", roster=None):
        """Initialize a Team (name, status, optional roster)."""
        self.school_name= school_name
        self.name=school_name
        self.status= status
        self.school=school_name
        self.game_stats={
            "points": 0,
            "rebounds": 0,
            "turnovers": 0,
            "ppg": 0
        }

        if roster is None:
            self.roster=[]
        else:
            self.roster=roster
        self.tournament_stats={"points": 0,
                               "rebounds": 0,
                               "turnovers": 0,
                               "wins": 0, 
                               "losses": 0,
                               "number_of_games": 0,
                               "ppg": 0
                               }

    def __eq__(self,other):
        """Team is equal only when name attributes are equal."""
        if isinstance(other, Team):
            return self.name==other.name
        return False

    def __str__(self):
        """Return team name and calculation (calculation= winning %)"""
        wins=self.tournament_stats.get("wins", 0)
        losses=self.tournament_stats.get("losses", 0)
        total= wins+losses
        if total==0:
            return f"{self.name}: 0.00"

        pct=wins/total
        return f"{self.name}: {pct:.2f}"

    def get_tournament_stats(self):
        """Tournament stats method.

        Return copy of tournament stats adding winning_percent.
        Keeps two decimals also.
        """
        stats_copy={}
        for key in self.tournament_stats:
            stats_copy[key]=self.tournament_stats[key]
        wins= stats_copy.get("wins", 0)
        losses= stats_copy.get("losses", 0)
        total=wins+losses

        if total==0:
            winning_percent= 0.00
        else:
            winning_percent=int((wins/total)*100)/100.0

        stats_copy["winning_percent"]=winning_percent
        return stats_copy

    def get_player(self, name, number):
        """Return Player in roster matching name and number, else None."""
        for player in self.roster:
            if player.name== name and player.number ==number:
                return player
        return None

    def add_player(self, player):
        """Return False if player already exists (same name/number).
        Else, add to roster and return True.
        """
        if self.get_player(player.name, player.number) is not None:
            return False
        self.roster.append(player)
        return True
