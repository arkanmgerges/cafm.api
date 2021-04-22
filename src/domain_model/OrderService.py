"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
from typing import List


class OrderService:
    def orderStringToListOfDict(self, orderString: str = "") -> List[dict]:
        if orderString == "":
            return []
        orderArray = [orderString.strip() for orderString in orderString.split(",")]
        result = []
        if len(orderArray) > 0:
            for item in orderArray:
                split = [item.strip() for item in item.split(":")]
                if len(split) > 1:
                    s1 = split[1]
                    if s1 != "asc" and s1 != "desc":
                        s1 = "asc"
                    result.append({"orderBy": split[0], "direction": s1})
                else:
                    result.append({"orderBy": split[0], "direction": "asc"})
        return result
