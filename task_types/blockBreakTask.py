from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class BlockBreakTask(AmountTask):

    identifier : str
    task_type = TaskType.BLOCK_BREAK

    amount : int

    @property
    def normalLore(self) -> str:
        return "Break %d blocks." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d blocks broken." % (self.identifier, self.amount)