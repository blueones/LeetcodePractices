startnode="a"
graph_edge = ["ab","ac","ad","ae","bf","bg","ch","ei","lz","yz","fm"]
class Solution:
    def breadthfirstsearch(self, graph_edge):

        rootnode="a"
        
        flaglist=[rootnode]
        while flaglist!=[]:
        # 2nd Layer
            child_list1=list()
            for edge in graph_edge:
                if edge[0] in flaglist:
                    child_list1.append(edge[1:])
            print(child_list1)
            flaglist=child_list1

            # 3rd Layer
#    '''         child_list2=list()
#         for node in child_list1:
#             for edge in graph_edge:
#                 if edge[0]==node:
#                     child_list2.append(edge[1:])
        # 4th Layer
        # child_list3=list()
        # for node in child_list2:
        #     for edge in graph_edge:
        #         if edge[0]==node:
        #             child_list3.append(edge[1:])


