### This is an extra thing that should theoretically make it easier
### to generate sequences of quests at a time

from typing import Callable, List
from baseclasses.baseReward import Reward
from baseclasses.dataclasses.amountTask import AmountTask
from baseclasses.baseQuest import Quest
from utils import simpleToRoman
from copy import copy

__all__ = ["QuestSequencer"]

class QuestSequencer(object):
    
    quest_id_prefix : str
    quest_name_prefix : str
    quest_base_task : AmountTask

    def __init__(self, id_prefix : str, name_prefix : str, base_task : AmountTask):
        self.quest_id_prefix = id_prefix
        self.quest_name_prefix = name_prefix
        self.quest_base_task = base_task

    def generateOccurences(self, occurences : int, amounts : List[int], rewards : List[Reward], *args, **kwargs) -> List[Quest]:
        
        quest_array = []

        for q in range(1, occurences+1, 1):

            t = copy(self.quest_base_task)
            t.amount = amounts[q - 1]

            quest_array.append(
                Quest(
                    quest_id = "%s%d" % (self.quest_id_prefix, q),
                    display_name = "%s %s" % (self.quest_name_prefix, simpleToRoman(q)),
                    tasks = [t,],
                    rewards = [rewards[q - 1],],
                    **kwargs
                )
            )
            
        return quest_array