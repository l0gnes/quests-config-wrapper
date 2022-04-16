from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class FarmingTask(AmountTask):

    identifier : str
    task_type = TaskType.FARMING

    amount : int

    @property
    def normalLore(self) -> str:
        return "Harvest %d crops." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d crops harvested." % (self.identifier, self.amount)