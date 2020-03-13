class Solution:
    def lengthLongestPath(self, input: str) -> int:
        #get a list of directories or files
        listofDirectory = input.split('\n')
        stackList = []
        resultMax = 0
        for item in listofDirectory:
            level = item.count("\t")
            while level < len(stackList):
                stackList.pop(-1)
            if stackList == []:
                currentLen = len(item)
            else:
                currentLen = stackList[-1]+len(item)-level+1
            stackList.append(currentLen)
            if "." in item:
                resultMax = max(currentLen,resultMax)
        return resultMax


print(Solution().lengthLongestPath("dir"))



class Solution2(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        '''
        use Stack: for each part seperated by '\n', we count the number of '\t' in it, which is the level it should be. Then we can check the size of the stack, if level ==size, then the last part in stack is the parent and we can add the current part to stack (actually we are adding the total length); otherwise if level<size, we have to pop out the stack
        '''
        stack = []
        ans = 0
        for s in input.split('\n'):
            level = s.count('\t')
            
            # make sure the top one in the stack is the parent level
            while len(stack)>level:
                stack.pop()
            
            # curr_len = prev_len+the length of s without '\t'+ one '/', notice that len('\t')=1 and len('/')=1
            if not stack:
                curr_len = len(s)-level+1
            else:
                curr_len = stack[-1]+len(s)-level+1
            stack.append(curr_len)
            
            # if we reach a file, we can check compare it with ans after removing the last '\'
            if '.' in s:
                ans = max(ans, curr_len-1)
        return ans
class Solution3:
    def lengthLongestPath(self, input: str) -> int:
        #more intuitive solution
        maxLen = 0
        lenDict = {-1:0}
        listOfLines= input.split("\n")
        for line in listOfLines:
            
            level = line.count("\t")
            if "." not in line:
                lenDict[level]= lenDict[level-1]+len(line)-level+1 #here we update/(overwrite) lenDict[level]
            elif "." in line:
                maxLen = max(maxLen, lenDict[level-1]+ len(line)-level)
        return maxLen