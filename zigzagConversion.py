class Solution:
    def convert(self, s, numRows):
        rows=list()
        lengthString=len(s)
        if numRows==1:
            return s
        
        
        for n in range(0,numRows):
            row1=list()
            for i in range(n,lengthString,2*numRows-2):
                rowItem1=s[i]
                row1.append(rowItem1)
                if (i+2*numRows-2-2*n)<lengthString and n!=0 and n!=(numRows-1):
                    rowItem1m=s[i+2*numRows-2-2*n]
                    row1.append(rowItem1m)
            rows.append(row1)
        resultString=str()
        for y in rows:
            for item in y:
                resultString+=item
        return resultString


print(Solution().convert("PAYPALISHIRING",3))
            
            