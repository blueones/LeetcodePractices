class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        balance = 0
        lenS = len(S)
        i = 0
        collector = ""
        collector_list =""
        while i<lenS:
            if balance == 0:
                collector = ""
            
            if S[i]=="(":
                collector+=S[i]
                balance +=1
                    
            elif S[i]==")":
                collector+=S[i]
                balance-=1
                if balance ==0:
                    collector_list+=collector[1:-1]
            i+=1
                    
                    
            
        return collector_list
class Solution1:
    def removeOuterParentheses(self, S: str) -> str:
        lenS = len(S)
        collector = ""
        result_collector = ""
        balance = 0
        for i in range(lenS):
            collector +=S[i]
            if S[i]=="(":
                balance +=1
            else:
                balance -=1
            if balance==0:
                result_collector += collector[1:-1]
                collector = ""
        return result_collector