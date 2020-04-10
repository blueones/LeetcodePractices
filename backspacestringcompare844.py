class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        #first instinct, time complexity O(n), space complexity(O(n))
        def helper(input_string):
            new_S = ""
            for letter in input_string:
                if letter =="#":
                    if new_S:
                        new_S=new_S[:-1]
                else:
                    new_S+=letter
            return new_S
        return helper(S)==helper(T)
class Solution1:
    def backspaceCompare(self,S,T):
        #improve iterate the array reversely
        # bad implementation
        #see LC solution from Solution2.
        len_S = len(S)
        len_T = len(T)
        pointer_S = len_S-1
        pointer_T = len_T-1
        back_S = 0
        back_T = 0
        s_target = t_target = ""
        while pointer_S>0 or pointer_T>0:
            
            if S[pointer_S]=="#":
                back_S+=1
                pointer_S-=1
                continue
            if back_S>0:
                while pointer_S>= 0 and back_S>0:
                    back_S-=1
                    pointer_S -=1
            else:
                s_target = S[pointer_S]
            if T[pointer_T]=="#":
                back_T+=1
                pointer_T-=1
                continue
            if back_T>0:
                while pointer_T>=0 and back_T>0:
                    back_T-=1
                    pointer_T -=1
            else:
                t_target = T[pointer_T]
            if s_target!= t_target:
                return False
            else:
                pointer_S -=1
                pointer_T-=1
        return True
            
class Solution2:
    def backspaceCompare(self,S,T):
        def helper(string_input,index):
            skip = 0
            return_value =""
            for i in range(index,-1,-1):
                if string_input[i]=="#":
                    skip+=1
                elif skip:
                    skip-=1
                else:
                    return_value = string_input[i]
                    break
            return return_value,i
        len_S = len(S)
        len_T = len(T)
        S_index = len_S-1
        T_index = len_T-1

        while S_index >=0 or T_index>=0:
            s_compare = t_compare = ""
            if S_index>=0:
                s_compare, S_index = helper(S,S_index)
            if T_index>=0:
                t_compare, T_index = helper(T,T_index)
            if s_compare!= t_compare:
                return False
            else:
                S_index -=1
                T_index -=1
        return True        


