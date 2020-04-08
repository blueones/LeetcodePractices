class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #happens to be the same as approach 1 in LC solution
        def helper(string_name):
            if string_name =="":
                return []
            dict_name = []
            section = [string_name[0]]
            flag = string_name[0]
        
            for letter in string_name:
                if letter!= flag:
                    dict_name.append(section[:])
                    section = []
                    flag = letter
                else:
                    section.append(letter)
            return dict_name
        processed_name = helper(name)
        target_name = helper(typed)
        len_processed = len(processed_name)
        len_target = len(target_name)
        if len_processed != len_target:
            return False
        for i in range(len_processed):
            if len(processed_name[i])>len(target_name[i]):
                return False
        return True
class Solution2:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        #happens to be the same as approach 1 in LC solution
        #implementation modified version.
        def helper(string_name):
            len_string = len(string_name)
            string_input = ""
            count = []
            pointer = 0
            for index in range(len_string):
                if index == len_string-1 or string_name[index]!= string_name[index+1]:
                    string_input+=string_name[index]
                    count.append(index - pointer+1)
                    pointer = index+1
            return Group(string_input,count)
        processed_name = helper(name)
        target_name = helper(typed)
        if processed_name.string_key != target_name.string_key:
            return False
        len_count = len(processed_name.string_key)
        for i in range(len_count):
            if processed_name.count[i]>target_name.count[i]:
                return False
        return True
class Group:
    def __init__(self,string_key, count):
        self.string_key = string_key
        self.count= count
class Solution1:
    def isLongPressedName(self,name,typed):
        #twopointersolution
        len_typed = len(typed)
        index_typed = 0
        for letter in name:
            if index_typed==len_typed:
                return False
            if typed[index_typed]!= letter:
                if typed[index_typed]!= typed[index_typed-1]:
                    return False
                while index_typed < len_typed and typed[index_typed]==typed[index_typed-1]:
                    index_typed += 1
                if index_typed == len_typed or typed[index_typed]!= letter:
                    return False
            index_typed+=1
        return True
                
