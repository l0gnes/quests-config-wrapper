from baseclasses.baseTask import Task
from baseclasses.dataclasses.certainBlockTask import CertainBlockTask
from enums.taskTypes import TaskType

class BlockPlaceCertainTask(CertainBlockTask):

    identifier : str
    task_type = TaskType.BLOCK_PLACE_CERTAIN

    amount : int
    block : str

    @property
    def normalLore(self) -> str:
        return "Place %d %s blocks." % (self.amount, self.block.title().replace("_", " "))

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d %s blocks placed." % (self.identifier, self.amount, self.block.title().replace("_", " "))