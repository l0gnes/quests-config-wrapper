from baseclasses.baseTask import Task
from enums.taskTypes import TaskType
from typing import List
from abc import ABC

class AmountTask(Task):

    identifier : str
    task_type : TaskType

    amount : int

    OUTPUT_VALUES = {
        "amount" : "amount"
    }

    def __init__(self, identifier : str, amount : int):
        super().__init__(identifier)
        self.amount = amount