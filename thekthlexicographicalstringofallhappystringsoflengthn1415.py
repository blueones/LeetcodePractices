class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        candidates = ["a","b","c"]
        self.result_list = []
        def helper(index, current_string,last_cha):
            if index == n:
                self.result_list.append(current_string)
            else:
                for candidate in candidates:
                    if (last_cha == "") or (last_cha and candidate != last_cha):
                        helper(index+1, current_string+candidate, candidate)
                        
        helper(0,"","")
        if len(self.result_list)>=k:
            return self.result_list[k-1]
        return ""
        