https://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
class Solution:
    def findPtwo(self,s,i):
        if i==0:
            return 2
        for a in range(1,i+1,1):
            if a<len(s)-i-1:
                #print("a now is",a)
                if s[i-a]!=s[i+a+1]:
                    return 2*(a-1)+2
                elif s[i-a]==s[i+a+1]:
                    if a==i:
                        return 2*a+2
                    continue
            else:
                #print ("return value is",2*(a-1)+2)
                return 2*(a-1)+2

    def findPone(self,s,i):
        if i==0:
            return 1
        for a in range(1,i+2,1):
            # print ("now a is",a)
            if a<=len(s)-i-1:
                if s[i-a]!=s[i+a]:
                    return 2*(a-1)+1
                elif s[i-a]==s[i+a]:
                    if a==i+1:
                        return 2*a-1
                    continue
            else: 
                return 2*(a-1)+1

        

    def longestPalindrome(self,s):
        lengthR=1
        flag=0
        if len(s)==1:
            return s
        for i in range(len(s)):
            #print("i is",i)
            if i==len(s)-1:
                lengthNew=1
            else:
                if s[i]==s[i+1]:
                    #print("string is",s,"and index is",i)
                    lengthNew=self.findPtwo(s,i)
                    #print("lengthNew now is",lengthNew)
                    if lengthNew>lengthR:
                        lengthR=lengthNew
                        flag=i
                #print("string is",s,"and index is",i)
                lengthNew=self.findPone(s,i)
                #print("lengthNew now is",lengthNew)
                if lengthNew>lengthR:
                    lengthR=lengthNew
                    flag=i
        if lengthR%2==1:
            # print("flag now is",flag,"lengthR is",lengthR)
            if flag==len(s)-1:
                # print("string now is",str(s[flag-(lengthR-1)/2:]))
                return str(s[flag-(lengthR-1)/2:])
            else:
                #print("flag-(lengthR-1)/2",flag-(lengthR-1)/2,"flag is",flag)
                return str(s[int(flag-(lengthR-1)/2):int(flag+(lengthR-1)/2)+1])
        elif lengthR%2==0:
            return str(s[int(flag-(lengthR)/2+1):int(flag+(lengthR)/2+1)])

# print(Solution().longestPalindrome("babab"))
# print(Solution().longestPalindrome("baba"))
# print(Solution().longestPalindrome("babac"))
#print(Solution().longestPalindrome("A"))
print(Solution().longestPalindrome("aaaaaaaaaaa"))