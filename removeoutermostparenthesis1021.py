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