class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strings= {}
        len_strs = len(strs)
        for i in range(len_strs):
            sorted_str = self.sortString(strs[i])
            if sorted_str in dict_strings:
                dict_strings[sorted_str].append(i)
            else:
                dict_strings[sorted_str] = [i]
        result_list = []
        for item in dict_strings:
            result_list.append([strs[index] for index in dict_strings[item]])
        return result_list
    def sortString(self,string_input):
        return_string = ""
        for item in sorted(string_input):
            return_string+=item
        return return_string