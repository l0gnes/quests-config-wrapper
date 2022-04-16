from os import PathLike
from typing import Dict, List
from baseclasses import Category
from baseclasses.baseQuest import Quest
from utils import dictArrayCombine
from ruamel.yaml import YAML
from copy import copy

class QuestingConfig(object):
    
    categories : Dict[str, Category] = {}
    quests : List[Quest] = []

    def addCategory(self, c : Category):

        if c.category_id in self.categories.keys():
            raise ValueError("Category ID has already been assigned.")

        self.categories[c.category_id] = c

    def fetchCategoryByID(self, c : str):

        if c in self.categories.keys():
            return self.categories[c]

        raise ValueError("Failed to find a category `%s`" % (c))

    def extendQuests(self, qs : List[Quest]):

        if any([not q.options_category for q in qs]):
            raise ValueError("Failed to extend quests: One of the quests provided does not have a category and therefore is invalid.")

        self.quests.extend(qs)

    def getCategoryFileExportContents(self):
        return {
            "categories" : dictArrayCombine([v.toDict() for v in list(self.categories.values())])
        }

    def exportCategoryFile(self, y : YAML, fp : PathLike):
        with open(fp, "w+") as f:
            y.dump(self.getCategoryFileExportContents(), f)

    def exportQuestFiles(self, y : YAML, fp : PathLike):
        for q in self.quests:
            with open("%s\\quests\\%s.yml" % (fp, q.quest_id), "w+") as f:
                x = copy(q.toDict())

                if x["options"]["requires"] is None:
                    del x["options"]["requires"]

                y.dump(x, f)
                

    def export(self, fp : PathLike):
        yaml_thing = YAML()

        self.exportCategoryFile(yaml_thing, "%s\\categories.yml" % (fp))
        self.exportQuestFiles(yaml_thing, fp)



