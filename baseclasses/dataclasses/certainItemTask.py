from baseclasses.dataclasses.amountTask import AmountTask
from enums.taskTypes import TaskType
from typing import List

class CertainItemTask(AmountTask):

    identifier : str
    task_type : TaskType

    amount : int
    item: str

    OUTPUT_VALUES = {
        "amount" : "amount",
        "item" : "item"
    }

    def __init__(self, identifier : str, amount : int, item : str):
        super().__init__(identifier, amount)
        self.amount = amount
        self.item = item