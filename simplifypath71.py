class Solution:
    def simplifyPath(self, path: str) -> str:
        list_levels = path.split("/")
        stack_levels = []
        for item in list_levels:
            if item =="..":
                if stack_levels:
                    stack_levels.pop(-1)
            elif item =="." or item=="":
                continue
            else:
                stack_levels.append(item)
        result_string = ""
        while stack_levels:
            result_string+="/"+stack_levels[0]
            stack_levels.pop(0)
        return result_string if result_string !="" else "/"
            