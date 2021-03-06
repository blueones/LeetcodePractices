# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''Dec 25th'''
class Solution1:
    def levelOrderBottom(self, root):
        self.root=root
        if self.root==None:
            return[]
        self.heightT=self.height(self.root)
        self.listLevel=[[] for i in range(1,self.heightT+1,1)]
        for i in range(self.heightT,0,-1):
            self.listLevel[self.heightT-i]=self.levelnodes(root,i)
            #print(self.listLevel)
        return self.listLevel

    def levelnodes(self,root,level):
        if root==None:
            return []
        elif root!=None:
            if level==1:
                return [root.val]
            elif level>1:
                return self.levelnodes(root.left,level-1)+self.levelnodes(root.right,level-1)

        
    def height(self,root):
        if root==None:
            return 0
        elif root!=None:
            heightN=1+max(self.height(root.left),self.height(root.right))
            return heightN
#Solution2: BFS. 
class Solution2:
    def levelOrderBottom(self, root):
        if root==None:
            return []
        if root!=None:
            queue=list()
            nextQueue=list()
            queue.append(root)
            resultlevel=[]
            resultlist=[]
            level=0
            while queue!=[]:
                newroot=queue.pop(0)
                resultlevel.append(newroot.val)
                if newroot.left!=None:
                    nextQueue.append(newroot.left)
                if newroot.right!=None:
                    nextQueue.append(newroot.right)
                if queue==[]:
                    queue=nextQueue.copy()
                    nextQueue=[]
                    resultlist.append(resultlevel)
                    resultlevel=[]
                    level+=1
        reverselist=[]
        lenResultlist=len(resultlist)
        for i in range(0,lenResultlist,1):
            reverselist.append(resultlist[lenResultlist-1-i])
        return reverselist

class Solution3():
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root==None:
            return []
        top = []
        queue = [root]
        while len(queue)>0:
            top.insert(0, [r.val for r in queue])
            n = len(queue)
            while n>0:
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                n = n-1
        return top

class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
'''Jan 19th '''
class Solution4():
    '''same as solution2'''
    def levelOrderBottom(self, root):
        if root == None:
            return []
        queueNodes = list()
        nextqueueNodes = list()
        queueNodes.append(root)
        listonlevel = list()
        listcurrentlevel = list()
        while queueNodes != []:
            #print(queueNodes[0].val)
            currentNode = queueNodes.pop(0)
            listcurrentlevel.append(currentNode.val)
            if currentNode.left:
                #print("left is ", currentNode.left.val)
                nextqueueNodes.append(currentNode.left)
            if currentNode.right:
                nextqueueNodes.append(currentNode.right)
            if queueNodes == []:
                queueNodes = nextqueueNodes
                nextqueueNodes = []
                listonlevel.append(listcurrentlevel)
                listcurrentlevel = []
        return listonlevel[::-1]

class Solution5():
    '''same as solution3'''
    def levelOrderBottom(self, root):
        '''this is Andy's solution. This involves a counter: n. for everylevel, it goes through n times to include nodes left and right. '''
        if root == None:
            return []
        queueLevel = list()
        queueLevel.append(root)
        resultList = list()
        while queueLevel != []:
            n = len(queueLevel)
            resultList.insert(0,[node.val for node in queueLevel])
            while n>0 :
                nodeCurrent = queueLevel.pop(0)
                queueLevel.append(nodeCurrent.left) if nodeCurrent.left else pass
                queueLevel.append(nodeCurrent.right) if nodeCurrent.right else pass
                n -= 1
        return resultList



SunnyTree = TreeNode(1)
SunnyTree.left = TreeNode(5)
SunnyTree.left.right = TreeNode(7)
SunnyTree.left.left = TreeNode(6)
SunnyTree.right = TreeNode(3)
SunnyTree.right.left = TreeNode(9)
SunnyTree.right.right = TreeNode(2)
SunnyTree.right.right.right = TreeNode(8)
print(Solution4().levelOrderBottom(SunnyTree))