from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class FishingTask(AmountTask):

    identifier : str
    task_type = TaskType.FISHING

    amount : int

    @property
    def normalLore(self) -> str:
        return "Catch %d fish." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d fish caught." % (self.identifier, self.amount)