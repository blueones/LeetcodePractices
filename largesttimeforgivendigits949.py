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
        #wrong. line 53 to 58 doesn't provide a descending order of results unfortunately. 
        A.sort(reverse=True)
        times = set()
        def checkValid(string_input):
            hour_input = int(string_input[:2])
            min_input = int(string_input[3:])
            if hour_input<24 and min_input<60:
                return True
            return False
        def helper(focus,current_tstring):
            if focus == 4:
                if checkValid(current_tstring):
                    times.append(current_tstring)
            if focus ==2:
                current_tstring+=":"
            for i in range(focus, len(A),1):
                A[i],A[focus]=A[focus],A[i]
                current_tstring+=str(A[focus])
                helper(focus+1,current_tstring)
                current_tstring= current_tstring[:-1]
                A[i],A[focus]=A[focus],A[i]
        helper(0,"")

        return helper(0,"")[0]
