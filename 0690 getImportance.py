"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        d={}
        for i in employees:
            d[i.id]=i
        self.ans=d[id].importance
        
        def aa(self,employees,ID):
            for j in d[ID].subordinates:
                self.ans=self.ans+self.getImportance(employees,j)
        aa(self,employees,id)
        return self.ans
