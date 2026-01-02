"""Double round robin for project_4."""
from match import Match
from round_robin import RoundRobin
from team import Team


class DoubleRoundRobin(RoundRobin):
    """Double round robin class.

    Double round robin where every team plays each other twice.
    Double Round robin is a subclass of RoundRobin.
    """

    def generate_matches(self):
        """Create match object for every time to play each other twice.

        Appends all match objects to matches and updates status
        to scheduled, and makes sure the teams play the game twice.
        """
        self.matches=[]
        for i in range(len(self.participants) - 1):
            for j in range(i+1, len(self.participants)):
                id1 = str(i) + str(j)
                team1 = Team(self.participants[i])
                team2 = Team(self.participants[j])
                self.matches.append(Match(id1, team1, team2))
        for i in range(len(self.participants) - 1):
            for j in range(i+1, len(self.participants)):
                id2 = str(j) + str(i)
                team1 = Team(self.participants[j])
                team2 = Team(self.participants[i])
                self.matches.append(Match(id2, team1, team2))

        self.status = "scheduled"
