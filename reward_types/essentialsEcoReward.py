from baseclasses.baseReward import Reward

class EssentialsEcoReward(Reward):
    
    amount : int

    @property
    def command(self):
        return "eco give {player} %d" % (self.amount)

    def __init__(self, amount : float):
        super()
        self.amount = amount

    @property
    def toString(self):
        return f"${self.amount:,}"