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
    def checkValidString(self, s) :
        #TLE solution. 
        def helper(string_check, index, count):
            if index == len(string_check) and count == 0:
                return True
            else:
                for i in range(index,len(string_check)):
                    if string_check[i] == "(":
                        count += 1

                    elif string_check[i] == "*":
                        return helper(string_check,i+1, count+1) or helper(string_check,i+1,count) or helper(string_check,i+1,count-1)
                    else:
                        if count>0:
                            count -= 1
                        else:
                            return False
                return count == 0
        
        return helper(s,0,0)
Solution1().checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")