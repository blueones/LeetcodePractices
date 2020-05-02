class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        def match(target, source):
            match_len = len(source)
            for i in range(match_len):
                if target[i] != source[i]:
                    return False
            return True
        dict_replacement = {}
        for i in range(len(indexes)):
            source = sources[i]
            target = targets[i]
            index = indexes[i]
            if match(S[index: index+len(source)], source):
                dict_replacement[index] = (len(source),target)
        visited = [False for i in range(len(S))]
        ans = ""
        for i in range(len(S)):
            if visited[i] == False and i in dict_replacement:
                for j in range(dict_replacement[i][0]):
                    visited[i+j] = True
                ans += dict_replacement[i][1]
            elif visited[i] == False:
                ans += S[i]
            
        return ans