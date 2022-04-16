from baseclasses.baseTask import Task
from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType

class ExperienceEarnTask(AmountTask):

    identifier : str
    task_type = TaskType.EXP_EARN

    amount : int

    @property
    def normalLore(self) -> str:
        return "Earn %d experience." % (self.amount)

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d experience earned." % (self.identifier, self.amount)