from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class MobKillingTask(AmountTask):

    identifier : str
    task_type = TaskType.MOB_KILLING

    amount : int

    @property
    def normalLore(self) -> str:
        return "Kill %d mobs." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d mobs killed." % (self.identifier, self.amount)