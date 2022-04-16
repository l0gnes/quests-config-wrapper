from baseclasses.baseTask import Task
from baseclasses.dataclasses.certainItemTask import CertainItemTask
from enums.taskTypes import TaskType

class FishingCertainTask(CertainItemTask):

    identifier : str
    task_type = TaskType.FISHING_CERTAIN

    amount : int
    item : str

    @property
    def normalLore(self) -> str:
        return "Catch %d %s." % (self.amount, self.item.title().replace("_", " "))

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d %s caught." % (self.identifier, self.amount, self.item.title().replace("_", " "))