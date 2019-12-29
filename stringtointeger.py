class Solution:
    def myAtoi(self, str):
        for i in str:
            if i ==" ":
                continue
            elif i=="+" or i=="-":
                return self
            elif i in range(10):

            else:
                return 0
        