"""Create roundrobin program for usage in tournament."""
from bracket import Bracket
from match import Match
from team import Team


class RoundRobin(Bracket):
    """Implement tournament format where each team plays eachother once."""

    def __init__(self, id, participants=None, status="not started", matches=None):
        """Initialize the roundrobin class."""
        super().__init__(id, participants, status, matches)
        self.standings={}
        self.teams={}
    def __eq__(self, other):
        """Return T f the same bracket_id is present in both brakcets."""
        if self.bracket_id==other.bracket_id:
            return isinstance(other, RoundRobin)
    def generate_matches(self):
        """Generate all matches for single round robin tournament.

        Each team plays every other team once and creates match objects
        for each team pairing and appends to list.
        """
        self.matches=[]
        for i in range(len(self.participants) - 1):
            for j in range(i+1, len(self.participants)):
                id = str(i) + str(j)
                team1 = Team(self.participants[i])
                team2 = Team(self.participants[j])
                self.matches.append(Match(id, team1, team2))
            self.status = "scheduled"

    def get_bracket_winner(self):
        """Determine team with the highest wins.

        Return team with most wins, if 2 or more teams tie,
        find the match and return winner, if there is more than 2,
        return the names of all 3 teams.
        """
        if self.status!= "completed":
            return []
        most_wins=0
        for name in self.standings:
            if self.standings[name]>most_wins:
                most_wins=self.standings[name]
        tie_team= []
        #checks to see if there is a tie present
        for name in self.standings:
            if self.standings[name]==most_wins:
        #adds each time when teams have the same number of wins
                tie_team.append(name)
        if len(tie_team)==1:
        #returns team object with the most wins
            return[self.teams[tie_team[0]]]
        if len(tie_team)==2:
        #creates two indexes to store each team
            team1=tie_team[0]
            team2=tie_team[1]

            for match in self.matches:
        #checks to see if the match is specifically a game between the 2 teams
        #and makes sure the order doesn't matter if they are flipped
                team1=match.team1
                team2=match.team2
                score1, score2=match.score
                if (match.team1.name==team1 and match.team2.name==team2) or \
                    (match.team1.name==team2 and match.team2.name==team1):
                    score_1, score_2= match.score
                if score_1>score_2:
                    return[self.teams[match.team1.name]]
                elif score_2>score_1:
                    return[self.teams[match.team2.name]]

        winners=[]
        #creates am empty list for winners when there are more than 2 teams
        #with the same number of wins
        for name in tie_team:
            winners.append(self.teams[name])
        return winners

    def update_standings(self):
        """Update tournament standings and team stats.

        Calculates wins, losses, total game scores for each team and
        updates standings and teams with values.
        """
        #initialize standings and teams
        self.standings={}
        self.teams={}
        for match in self.matches:
            team1= match.team1
            team2= match.team2
            self.standings[team1.name]=0
            self.standings[team2.name]=0
            self.teams[team1.name]= Team(team1.name)
            self.teams[team2.name]= Team(team2.name)
        #updating score, standings, teams
        for match in self.matches:
            team1= match.team1
            team2= match.team2
            score1= team1.game_stats['points']
            score2= team2.game_stats['points']
            if score1> score2:
                self.standings[team1.name]+=1
                self.teams[team1.name].tournament_stats['wins']+=1
                self.teams[team2.name].tournament_stats['losses']+=1

            else:
                self.standings[team2.name]+=1
                self.teams[team2.name].tournament_stats['wins']+=1
                self.teams[team1.name].tournament_stats['losses']+=1
            match.score= (score1, score2)
            self.teams[team1.name].tournament_stats['points']+=\
            team1.game_stats['points']
            self.teams[team1.name].tournament_stats['rebounds']+=\
            team1.game_stats['rebounds']
            self.teams[team1.name].tournament_stats['turnovers']+=\
            team1.game_stats['turnovers']
            self.teams[team1.name].tournament_stats['number_of_games']+= 1

            self.teams[team2.name].tournament_stats['points']+=\
            team2.game_stats['points']
            self.teams[team2.name].tournament_stats['rebounds']+=\
            team2.game_stats['rebounds']
            self.teams[team2.name].tournament_stats['turnovers']+=\
            team2.game_stats['turnovers']
            self.teams[team2.name].tournament_stats['number_of_games']+= 1



