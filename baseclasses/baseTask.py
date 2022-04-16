from abc import ABC, abstractmethod, abstractproperty
from enums.taskTypes import TaskType
from typing import List, Optional
from copy import copy

class Task(ABC):

    identifier : str
    task_type : TaskType

    OUTPUT_VALUES = {
        # config key : object attr
    }

    @property
    def normalLore(self) -> str:
        raise NotImplemented

    @property
    def startedLore(self) -> str:
        raise NotImplemented

    def __init__(self, identifier : str):
        self.identifier = identifier

    def toDict(self) -> dict:

        attr = {
                k : self.__getattribute__(v) for k, v in self.OUTPUT_VALUES.items()
        }
        attr.update({"type": self.task_type.value})

        return {
            self.identifier : attr
        } 