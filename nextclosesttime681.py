class Solution:
    def nextClosestTime(self, time: str) -> str:
        array_digits = set()
        digits = time[:2]+time[3:]
        for digit in digits:
            array_digits.add(digit)
        def checkValid(string_input):
            min_num = int(string_input[0])*10+int(string_input[1])
            second_num = int(string_input[2])*10+int(string_input[3])
            if min_num<24 and second_num<60:
                return True, min_num*100+second_num
            return False,-1
        current_time_num = checkValid(time[:2]+time[3:])[1] 
        self.current_next = 24*100
        self.min_time_num = 24*100
        def helper(current_string,index,array_digits,min_time_num,current_next):
            if index ==4:
                
                validness, time_num = checkValid(current_string)
                if validness:
                    
                    self.min_time_num = min(self.min_time_num, time_num)
                    if time_num > current_time_num:
                        
                        self.current_next = min(self.current_next,time_num)
                       
            else:
                for digit in array_digits:
                    current_string+=digit
                    helper(current_string,index+1,array_digits,self.min_time_num,self.current_next)
                    current_string=current_string[:-1]
        helper("",0,array_digits,self.min_time_num,self.current_next)
        if self.current_next< 2400:
            time_num_final=self.current_next
        else:
            time_num_final= self.min_time_num
        return "{:02}:{:02}".format(*divmod(time_num_final,100))
class Solution1:
    def nextClosestTime(self,time):
        #after reviewing LC solutions.
        