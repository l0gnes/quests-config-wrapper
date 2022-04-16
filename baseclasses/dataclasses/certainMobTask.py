from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType
from typing import List

class CertainMobTask(AmountTask):

    identifier : str
    task_type : TaskType

    amount : int
    mob: str

    OUTPUT_VALUES = {
        "amount" : "amount",
        "mob" : "mob"
    }

    def __init__(self, identifier : str, amount : int, mob : str):
        super().__init__(identifier, amount)
        self.amount = amount
        self.mob = mob