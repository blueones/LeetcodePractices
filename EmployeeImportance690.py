
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        for employee in employees:
            if employee.id==id:
                importance=employee.importance
                wholeimportanceSub=0
                for employeeSub in employee.subordinates:
                    importanceSub=self.getImportance(employees,employeeSub)
                    wholeimportanceSub+=importanceSub
                importanceF=importance+wholeimportanceSub
        return importanceF






employees1=[[1,2,[2]], [2,3,[]]]
id=2
Solution().getImportance(employees1,id)