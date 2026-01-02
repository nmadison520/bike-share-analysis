from participant import Participant

class Player(Participant):
    def __init__(self, name, number, school, status="healthy", position=None):
        super().__init___(name=name, id=number, status=status, school=school)
        self.number= number
        self.position=position
    
    def __eq__(self, player2):
        """
        This will return T if two player objects equate to each other when their attributes-
        including name, school, number attributes are equal.
        """
        if isinstance(player2, Player):
            return (self.name== player2.name and 
                    self.number== player2.number and 
                    self.school== player2.school)
            return False
        
    def get_tournament_stats(self):
        """
        Make copy of stats from tournament attribute. 
        Add points per game to the copy (ppg).
        Rounds to two decimal places, and returns copy of 
        tournament stats as a dict.
        """
        copy_stats=self.tournament_copy_stats()
        total_points=copy_stats.get("total points", 0)
        total_games=copy_stats.get("total number of games", 0)

        if total_games==0:
            ppg=0.00
        else:
            ppg=total_points/total_games
            ppg=int(ppg*100)/100.0
        copy_stats["ppg"]=ppg
        return copy_stats
