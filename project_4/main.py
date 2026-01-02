"""Main program for project_4."""
from match_reader import MatchReader
from round_robin import RoundRobin

def main():
    """Main function.

    Reads data from round robin matches, and uses matchreader class
    to do so. Determines winner using the roundrobin class and prints
    the name of the winner. Also analyzes two other statistics and
    prints results.
    """
    reader= MatchReader("round_robin_matches.csv")
    match0= reader.matches[0]
    print(match0.team1.name, match0.team2.name)
    team1=match0.team1
    print(team1.name, team1.game_stats['points'])

if __name__== '__main__':
    main()

