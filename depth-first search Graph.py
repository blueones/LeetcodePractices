startnode="a"
graph_edge = ["ab","ba","ac","ad","ae","bf","bg","ch","ei","lz","yz","fm"]
class Solution:
    def gothruList(self,graph_edge):
        startnode=graph_edge[0][0]
    def depthfirstsearchrun(self, graph_edge,startnode):
        #go through each edge
        self.depthfirstsearch(graph_edge,startnode,[],[startnode])
        
    def depthfirstsearch(self,graph_edge,startnode,visited,selfchain):
        for edge in graph_edge:
            if edge in visited:
                continue
            if edge[0]==startnode and edge[1] not in selfchain:
                newitem=[edge[1]]
                newselfchain=selfchain+newitem
                #print("newchain is ",newselfchain)

                visited.append(edge)
                print(edge)
                self.depthfirstsearch(graph_edge,edge[1],visited,newselfchain)
            if edge[0]==startnode and edge[1] in selfchain:
                continue
            
        return visited


            



Solution().depthfirstsearchrun(graph_edge,startnode)
