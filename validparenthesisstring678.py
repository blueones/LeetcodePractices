class Solution:
    def checkValidString(self, s: str) -> bool:
        high = 0
        low = 0
        for cha in s:
            high += 1 if cha != ")" else -1
            low += 1 if cha =="(" else -1
            if high<0:
                return False
            low = max(low, 0)
        if low>0:
            return False
        
        return True


class Solution1:
    def checkValidString(self, s: str) -> bool:
        stack_check = []
        len_s = len(s)
        self.ans = True
        def helper(string_check, index, stack):
            if index == len_s:
                self.ans = True
            else:
                
                if string_check[index] == "(":
                    stack.append("(")
                    helper(string_check,index+1, stack)

                elif string_check[index] == "*":
                    stack.append("(")
                    helper(string_check, index+1, stack)
                    stack.pop(-1)
                    if stack:
                        stack.pop(-1)
                        helper(string_check,index+1,stack)
                else:
                    if stack:
                        stack.pop(-1)

                    else:
                        return False
        
        helper(s,0,[])
        if ans_list:
            return True
                        