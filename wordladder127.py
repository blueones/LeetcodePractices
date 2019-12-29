class Solution1:
    def ladderLength(self, beginWord, endWord, wordList):
#1. create a graph with the data structure of adjacent list with the word as its index. 
    # all the neighbors are supposed to be words that contain only one letter different from the index word.
    #2. start with startword, use BFS to go thru the path. remember to mark visited. 
    #3. create a dictionary that store the distance from startword. if in the end, the endword was not marked, then return 0.
    #also if the endword is not in the graph, return 0
        if endWord not in wordList:
            return 0
        self.graphlist=Graph(wordList)
        self.adjList=self.graphlist.adj
        self.wordL=len(beginWord)
        self.nodesNum=self.graphlist.NumNodes
        self.marked={word:False for word in wordList}
        self.distance={word:0 for word in wordList}
        #for all words in wordlist, go through and create adjlist. check if neighbor by doing neighborchecking.
        for wordIndex in range(self.nodesNum-1):
            for wordNeighborIndex in range(wordIndex+1,self.nodesNum,1):
                if self.neighborChecking(wordList[wordIndex],wordList[wordNeighborIndex]):
                    self.graphlist.addEdge(wordList[wordIndex],wordList[wordNeighborIndex])
                    self.graphlist.addEdge(wordList[wordNeighborIndex],wordList[wordIndex])
        BFSlist=list()

        for word in wordList:
            if self.neighborChecking(beginWord,word):
                BFSlist.append(word)
                self.marked[word]=True
                self.distance[word]=2
        while BFSlist!=[]:
            wordCheck=BFSlist.pop(0)
            print("the word being checked is ",wordCheck)
            for neighborNode in self.adjList[wordCheck]:
                if self.marked[neighborNode]==True:
                    continue
                else:
                    self.marked[neighborNode]=True
                    self.distance[neighborNode]=self.distance[wordCheck]+1
                    print("the neighbor being checked is ",neighborNode, "it's distance is ", self.distance[neighborNode])
                    BFSlist.append(neighborNode)
        if self.marked[endWord]==False:
            return 0
        return self.distance[endWord]

        



    def neighborChecking(self,wordIndex, wordNeighbor):
        counter=0
        for i in range(self.wordL):
            if wordIndex[i]==wordNeighbor[i]:
                counter+=1
        if counter==self.wordL-1:
            return True
        return False


        
from collections import defaultdict        
class Solution2:
    def ladderLength(self, beginWord, endWord, wordList):
#1. create a graph with the data structure of adjacent list with the word as its index. 
    # all the neighbors are supposed to be words that contain only one letter different from the index word.
    #2. start with startword, use BFS to go thru the path. remember to mark visited. 
    #3. create a dictionary that store the distance from startword. if in the end, the endword was not marked, then return 0.
    #also if the endword is not in the graph, return 0
#2. use leetcode's solution of creating a dictionary of key being a template of word, value being a list of words that fit that template.so these words are neighbors. 
#   use this data structure to assess neighboring. instead of O(N^2), this method is O(M*N), slightly better.
        if endWord not in wordList:
            return 0
        self.graphlist=Graph(wordList)
        self.adjList=self.graphlist.adj
        self.wordL=len(beginWord)
        self.nodesNum=self.graphlist.NumNodes
        self.marked={word:False for word in wordList}
        self.distance={word:0 for word in wordList}
        #for all words in wordlist, go through and create adjlist. check if neighbor by doing neighborchecking.
        self.listofwordT=defaultdict(list)
        for word in wordList:
            for i in range(self.wordL):
                self.listofwordT[word[:i]+"1"+word[i+1:]].append(word)
        
        BFSlist=list()
        for word in wordList:
            if self.neighborChecking(beginWord,word):
                BFSlist.append(word)
                self.marked[word]=True
                self.distance[word]=2
        while BFSlist!=[]:
            wordCheck=BFSlist.pop(0)
            #print("the word being checked is ",wordCheck)
            for n in range(self.wordL):
                wordCheckInter=wordCheck[:n]+"1"+wordCheck[n+1:]
                for neighborsN in self.listofwordT[wordCheckInter]:
                    if self.marked[neighborsN]==True:
                        continue
                    else:
                        self.marked[neighborsN]=True
                        self.distance[neighborsN]=self.distance[wordCheck]+1
                        if neighborsN==endWord:
                            return self.distance[endWord]
                        #print("the neighbor being checked is ",neighborsN, "it's distance is ", self.distance[neighborsN])
                        BFSlist.append(neighborsN)
        if self.marked[endWord]==False:
            return 0
        return self.distance[endWord]

        



    def neighborChecking(self,wordIndex, wordNeighbor):
        for i in range(self.wordL):
            intermidiate=wordIndex[:i]+"1"+wordIndex[i+1:]
            if wordNeighbor in self.listofwordT[intermidiate]:
                return True
        return False    






class Graph:
    def __init__(self,listofnodes):
        self.adj={node:[] for node in listofnodes}
        self.NumNodes=len(listofnodes)

    def addEdge(self,nodeindex,nodeneighbor):
        self.adj[nodeindex].append(nodeneighbor)



Solution2().ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"])