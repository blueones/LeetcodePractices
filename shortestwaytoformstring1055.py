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
Solution().shortestWay("abc","abcbc")