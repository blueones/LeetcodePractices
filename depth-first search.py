class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

SunnyTree = TreeNode(1)
SunnyTree.left = TreeNode(5)
SunnyTree.left.right = TreeNode(7)
SunnyTree.left.left = TreeNode(6)
SunnyTree.right = TreeNode(3)
SunnyTree.right.left = TreeNode(9)
SunnyTree.right.right = TreeNode(2)
SunnyTree.right.right.right = TreeNode(8)

# 15673928
# 65719328
# 67598231

class Solution:
	def recursiveDFSQ(self,root):
		print(root.val)
		#do something
		if root.left!=None:
			self.recursiveDFSQ(root.left)           
		if root.right!=None:
			self.recursiveDFSQ(root.right)

	def recursiveDFSZ(self,root):
		#do something
		if root.left!=None:
			self.recursiveDFSZ(root.left)    
		print(root.val)       
		if root.right!=None:
			self.recursiveDFSZ(root.right)

	def recursiveDFSH(self,root):
		if root.left!=None:
			self.recursiveDFSH(root.left)           
		if root.right!=None:
			self.recursiveDFSH(root.right)
		print(root.val)
		
		

				


	def stackDFSQ(self,root):
		#Preorder traversal
		stackL=list()
		stackL.append(root)
		
		while len(stackL)>0:
			currentNode=stackL.pop(-1)
			if currentNode.right!=None:
				stackL.append(currentNode.right)
			if currentNode.left!=None:
				stackL.append(currentNode.left)
			
			print(currentNode.val)
	def stackDFSZ(self,root):
		stackL = list()
		while True:
			
			if root:
				stackL.append(root)
				root = root.left

			elif stackL != []:
				
				currentNode = stackL.pop(-1)
				print(currentNode.val)
				root = currentNode.right

			else:
				break
			

	def stackDFSH(self,root):
		stackL1 = list()
		stackL2 = list()
		stackL1.append(root)
		while stackL1 != []:
			currentNode = stackL1.pop(-1)
			stackL2.append(currentNode)
			if currentNode.left:
				stackL1.append(currentNode.left)
			if currentNode.right:
				stackL1.append(currentNode.right)	
		while stackL2 != []:
			popNode = stackL2.pop(-1)
			print(popNode.val)	

Solution().stackDFSH(SunnyTree)