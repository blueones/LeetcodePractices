class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits_n = []
        while n>0:
            digits_n.append(n%10)
            n=n//10
        lenN = len(digits_n)
        digits_n.reverse()
        index = lenN -1
        end = False
        result_int = 0
        while index> 0:
            if digits_n[index]>digits_n[index-1]:
                end = True
                break
            index -= 1
        if not end:
            return -1
        exchange_index = index-1
        i = index
        while i < lenN:
            if digits_n[exchange_index]>=digits_n[i]:
                cut_index = i-1
                break
            i+=1
        if i == lenN:
            digits_n[-1],digits_n[exchange_index]= digits_n[exchange_index],digits_n[-1]
            new_digits_n = digits_n[exchange_index+1:]+[digits_n[exchange_index]]
            new_digits_n.reverse()
            
            digits_n =digits_n[:exchange_index]+new_digits_n
        else:
            digits_n[cut_index],digits_n[exchange_index]= digits_n[exchange_index],digits_n[cut_index]
            new_digits_n = digits_n[exchange_index+1:]
            new_digits_n.reverse()
            digits_n =digits_n[:exchange_index+1]+new_digits_n
        for digit in digits_n:
            result_int=result_int*10+digit
        if result_int > 2**31-1:
            return -1
        return result_int
print(Solution().nextGreaterElement(12))