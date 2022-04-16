class ItemReward(object):
    
    item : str
    amount : int

    @property
    def command(self):
        return "give {player} %s %d" % (self.item, self.amount)

    @property
    def toString(self):
        return f"{self.amount}x {self.item.title()}"

    def __init__(self, item : str, amount : int):
        super()
        self.item = item
        self.amount = amount