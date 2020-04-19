class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        #recursion solution. TLE
        croak = "croak"
        def helper(string_input):
            if string_input[0] != "c":
                return -1
            ans = ""
            counter = 0
            for cha in string_input:
                if cha == croak[counter]:
                    counter += 1
                else:
                    ans+=cha
                counter = counter%5
            if ans:
                result= helper(ans)
                if result == -1:
                    return -1
                else:
                    return result+1
                
            elif ans == "":
                if counter == 0:
                    return 1
                return -1
        return helper(croakOfFrogs)
