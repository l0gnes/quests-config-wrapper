from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class BlockPlaceTask(AmountTask):

    identifier : str
    task_type = TaskType.BLOCK_PLACE

    amount : int

    @property
    def normalLore(self) -> str:
        return "Place %d blocks." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d blocks placed." % (self.identifier, self.amount)