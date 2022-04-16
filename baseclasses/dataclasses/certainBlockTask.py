from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType
from typing import List

class CertainBlockTask(AmountTask):

    identifier : str
    task_type : TaskType

    amount : int
    block : str

    OUTPUT_VALUES = {
        "amount" : "amount",
        "block" : "block"
    }

    def __init__(self, identifier : str, amount : int, block : str):
        super().__init__(identifier, amount)
        self.amount = amount
        self.block = block