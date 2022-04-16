from baseclasses.baseTask import Task
from baseclasses.baseReward import Reward
from baseclasses.baseCategory import Category
from typing import List, Optional
from utils import dictArrayCombine

class Quest():
    
    tasks : List[Task] = []

    quest_id : str

    display_name : str = "Unnamed Quest"
    display_item : str = "DIRT"

    rewards : List[Reward] = []

    options_requires : Optional[List[Task]] = None
    options_repeatable : bool = False
    options_category : Category = None
    options_sort_order : int = None

    def __init__(self, quest_id : str, display_name : str, display_item : str, *, tasks : List[Task] = [], rewards : List[Reward] = []):
        self.quest_id = quest_id
        self.display_name = display_name
        self.display_item = display_item
        self.tasks = tasks
        self.rewards = rewards

    @property
    def started_lore(self):
        returnValue = ["", "&7Your current progression:"]

        for t in self.tasks:
            returnValue.append(
                "&7- %s" % (t.startedLore)
            )

        return returnValue

    @property
    def normal_lore(self):
        returnValue = ["&7Quest requirements: ",]

        for t in self.tasks:
            returnValue.append(
                "&7- %s" % (t.normalLore)
            )

        returnValue.extend(["", "&7Rewards:"])

        for r in self.rewards:
            returnValue.append(
                "&7- %s" % (r.toString)
            )

        return returnValue

    def toDict(self):
        return {
            "tasks" : dictArrayCombine([k.toDict() for k in self.tasks]),
            "display" : {
                "name" : self.display_name,
                "type" : self.display_item,
                "lore-normal" : self.normal_lore,
                "lore-started" : self.started_lore
            },
            "rewards" : [r.command for r in self.rewards],
            "options" : {
                "category" : self.options_category.category_id,
                "repeatable" : self.options_repeatable,
                "requires" : None if not self.options_requires else [self.options_requires.quest_id,],
                "sort-order" : self.options_sort_order
            }
        }
        

