from baseclasses.baseTask import Task
from baseclasses.dataclasses.certainMobTask import CertainMobTask
from enums.taskTypes import TaskType

class MobKillingCertainTask(CertainMobTask):

    identifier : str
    task_type = TaskType.MOB_KILLING_CERTAIN

    amount : int
    mob : str

    @property
    def normalLore(self) -> str:
        return "Kill %d %s." % (self.amount, self.mob.title().replace("_", " "))

    @property
    def startedLore(self) -> str:
        return "{%s:progress}/%d %s killed." % (self.identifier, self.amount, self.mob.title().replace("_", " "))