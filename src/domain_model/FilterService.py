"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List


class FilterService:
    def filterStringToListOfDict(self, filtersString: str = "") -> List[dict]:
        if filtersString == "":
            return []
        filterArray = [filterString.strip() for filterString in filtersString.split(",")]
        result = []
        if len(filterArray) > 0:
            for item in filterArray:
                split = [item.strip() for item in item.split(":")]
                result.append({"key": split[0], "value": split[1]})
        return result
