from die import Die

class TwoDice(Die):
    def __init__(self, sides=6):
        super().__init__(sides)
        self.dice1= Die(self.sides)
        self.dice2= Die(self.sides)

    def roll(self):
        return (self.dice1.roll(), self.dice2.roll)
    
    def total(self):
        roll=self.roll()
        return f'Roll: {roll}\nTotal: {sum(roll)}'

if __name__ == "__main__":
    two_dice = TwoDice()
    #print(two_dice.roll())
    print(two_dice.total())