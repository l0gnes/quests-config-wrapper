from baseclasses.baseTask import Task
from baseclasses.dataclasses.certainBlockTask import CertainBlockTask
from enums.taskTypes import TaskType

class FarmingCertainTask(CertainBlockTask):

    identifier : str
    task_type = TaskType.FARMING_CERTAIN

    amount : int
    block : str

    @property
    def normalLore(self) -> str:
        return "Harvest %d %s." % (self.amount, self.block.title().replace("_", " "))

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d %s harvested." % (self.identifier, self.amount, self.block.title().replace("_", " "))