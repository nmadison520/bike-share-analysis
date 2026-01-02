from participant import Participant

class Team(Participant):
    def __init__(self, school_name, status= "active", roster=None):
        super().__init__(name=school_name, id=None, status=status, school=school_name)
        if roster is None:
            self.roster=[]
        else:
            self.roster=roster
        self.tournament_stats={"wins": 0, "losses": 0}

    def __eq__(self,player2):
        """
        Team is equal only when name attributes are equal.
        """
        if isinstance(player2, Team):
            return self.name==player2.name
        return False
    def get_tournament_stats(self):
        """
        Return copy of tournament stats adding winning_percent.
        Keeps two decimals also.
        """
        copy_stats= self.tournament_stats.copy()
        wins= copy_stats.get("wins", 0)
        losses= copy_stats.get("losses", 0)
        total=wins+losses

        if total==0:
            w_p= 0.00
        else:
            w_p=wins/total
            w_p=int(w_p*100)/100.0
        
        copy_stats["winning percent"]=w_p
        return copy_stats

    def find_player(self, name, number):
        """
        Return Player in roster matching name and number, else return None.
        """
        for player in self.roster:
            if player.name== name and player.number ==number:
                return player
        return None
    
    def add_player(self, player):
        """
        Return False if player already exists (same name/number).
        Else, add to roster and return True.
        """
        exist_= self.find_player(player.name, player.number)
        if exist_ is not None:
            return False
        self.roster.append(player)
        return True