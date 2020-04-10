class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        #permutation get 4*3*2*1 variations, then compare
        list_possible = []
        def helper_function(list_current,num,list_input):
            #input a list, output a combination of this a list of list
            if num == 0:
                list_possible.append(list_current)
            else:
                for i in range(num):
                    rest_list = list_input[:i]+list_input[i+1:]
                    list_current.append(list_input[i])
                    helper_function(list_current[:],num-1,rest_list)
                    list_current.pop(-1)
        helper_function([],4,A)
        max_time = -1
        for item in list_possible:
            hour = item[0]*10+item[1]
            if hour <24:
                min_now = item[2]*10+item[3]
                if min_now <60:
                    time_now = hour*100+min_now
                    max_time = max(max_time,time_now)
        if max_time ==-1:
            return ""
        time =[0,0,0,0]
        index = 3
        while max_time>0:
            time[index]=(max_time%10)
            max_time = max_time//10
            index-=1
        final = ""
        for i in range(4):
            final+=str(time[i])
        return final[:2]+":"+final[2:]
class Solution1:
    def largestTimeFromDigits(self,A):
        permutation = []
        def helper(focus):
            if focus == 4:
                permutation.append(A[:])
            else:
                for i in range(focus, 4, 1):
                    A[focus],A[i]= A[i], A[focus]
                    helper(focus+1)
                    A[focus],A[i]= A[i], A[focus]
        helper(0)
        answer = 0
        for array in permutation:
            if array[0]*10+array[1]<24 and array[2]*10+array[3]<60:
                current_time = (array[0]*10+array[1])*100+array[2]*10+array[3]
                answer = max(answer,current_time)
        return "{:02}:{:02}".format(*divmod(answer,100)) if answer>=0 else "" #mark this string formatting. 
        

