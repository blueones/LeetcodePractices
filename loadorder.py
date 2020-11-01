class Solution:
    def __init__(self, dependency_list):
        self.dependency_list = dependency_list
    def find_load_order(self, input_app):
        dependency_dict = {i["name"]:i["dependencies"] for i in self.dependency_list}
        self.order = []
        to_load = dependency_dict[input_app]
        loaded = {i:False for i in to_load}
        def dfs_helper(app):
            if app in dependency_dict:
                for pre_app in dependency_dict[app]:
                    if pre_app not in loaded or loaded[pre_app] == False:
                        dfs_helper(pre_app)
            self.order.append(app)
            loaded[app] = True
        dfs_helper(input_app)
        return self.order[:-1]
dependency_list = [
    {
        "name":"express",
        "dependencies":["router","query","route","application","response"]
    },
    {
        "name":"router",
        "dependencies":["route","layer"]
    },
    {
        "name":"route",
        "dependencies":["layer"]
    },
    {
        "name":"application",
        "dependencies":["router","query","init","view","utils","map"]
    },
    {
        "name":"response",
        "dependencies":["utils"]
    },
        ]
print(Solution(dependency_list).find_load_order("application"))

