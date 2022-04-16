
from typing import List

__all__ = ["Category"]

class Category(object):
    
    quests : List["Quest"] = []
    category_id : str

    display_category_name : str = "A category"
    display_category_item : str = "WOODEN_PICKAXE"

    def __init__(self, category_id : str, category_name : str, category_item : str) -> None:
        self.category_id = category_id
        self.display_category_item = category_item
        self.display_category_name = category_name

    def extendNoRequire(self, L : List["Quest"]):
        n = len(self.quests)
        for q in L:
            q.options_category = self
            q.options_sort_order = n
            n += 1
        self.quests.extend(L)

    def extendWithRequire(self, L : List["Quest"]):
        last = None
        n = len(self.quests)
        for index, q in enumerate(L):
            q.options_category = self
            q.options_sort_order = len(self.quests) + index
            q.options_requires = last
            last = q
        self.quests.extend(L)

    def __len__(self):
        return len(self.quests)

    def toDict(self):
        return {
            self.category_id : {
                "display" : {
                    "name" : self.display_category_name,
                    "type" : self.display_category_item,
                    "lore" : ["- Sample text here", "- Blah blah blah"] # I'm not building in support for this, die.
                }
            }
        }