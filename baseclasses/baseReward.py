from abc import ABC, abstractmethod

class Reward(ABC):

    @property
    def command(self):
        pass

    @property
    def toString(self):
        pass