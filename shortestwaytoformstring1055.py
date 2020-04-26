class Solution:
    def shortestWay(self, source, target):
        #two pointer solution. 
        #when you are trying to mark position in a dictionary and there are duplicates so it's hard to manuver, think if you can use pointer.
        source_pointer = target_pointer = 0
        target_len = len(target)
        source_len = len(source)
        set_source = set()
        for chara in source:
            set_source.add(chara)

        count = 1
        while target_pointer < target_len:
            if target[target_pointer] in set_source:
                if source_pointer == source_len:
                    source_pointer = 0
                    count += 1
                while source_pointer < source_len and source[source_pointer]!= target[target_pointer]:
                    source_pointer += 1
                if source_pointer == source_len:
                    continue
                else:
                    source_pointer += 1
                    target_pointer += 1
            else:
                return -1
        return count




import collections
class Solution1:
    def shortestWay(self,source, target):
        source_index = collections.defaultdict(list)
        for index_cha in range(len(source)):
            source_index[source[index_cha]].append(index_cha)
        times = 1
        i = -1
        for cha in target:
            if cha in source_index:
                #find first in source_index[cha] that's larger than i
                #update i 
                new_index = self.find(i,source_index[cha])
                if new_index != -1:
                    i = source_index[cha][new_index]
                else:
                    times+=1
                    i = source_index[cha][0]
            else:
                return -1
        return times
    def find(self, left, list_match):
        len_list = len(list_match)
        i = 0
        while i < len_list:
            if list_match[i] <= left:
                i+=1
            else:
                break
        if i == len_list:
            return -1
        else:
            return i

class Solution2:
    #improved solution1 
    def shortestWay(self,source, target):
        source_index = collections.defaultdict(list)
        for i, cha in enumerate(source):
            source_index[cha].append(i)
        times = 1
        i = -1
        for cha in target:
            if cha in source_index:
                #find first in source_index[cha] that's larger than i
                #update i 
                new_index = self.find(i,source_index[cha])
                if new_index != -1:
                    i = source_index[cha][new_index]
                else:
                    times+=1
                    i = source_index[cha][0]
            else:
                return -1
        return times
    def find(self, left, list_match):
        len_list = len(list_match)
        i = 0
        while i < len_list:
            if list_match[i] <= left:
                i+=1
            else:
                break
        if i == len_list:
            return -1
        else:
            return i



        

Solution1().shortestWay("abc","abcbc")
    