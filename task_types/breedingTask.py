from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class BreedingTask(AmountTask):

    identifier : str
    task_type = TaskType.BREEDING

    amount : int

    @property
    def normalLore(self) -> str:
        return "Breed %d animals." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d animals bred." % (self.identifier, self.amount)