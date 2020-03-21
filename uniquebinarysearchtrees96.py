class Solution:
    def numTrees(self, n: int) -> int:
        # Intuition

        # The problem can be solved in a dynamic programming way.

        # Given a sorted sequence 1 ... n, to construct a Binary Search Tree (BST) out of the sequence, 
        # we could enumerate each number i in the sequence, and use the number as the root, 
        # then, the subsequence 1 ... (i-1) on its left side would lay on the left branch of the root, 
        # and similarly the right subsequence (i+1) ... n lay on the right branch of the root. 
        # We then can construct the subtree from the subsequence recursively. 
        # Through the above approach, we could be assured that the BST that we construct are all unique, 
        # since they start from unique roots.

        #nodeIndex is from 1 to n
        def createTree(allNodes):
            if allNodes>0:
                numberT = 0
                for node in range(1,allNodes+1):
                    leftS = node -1
                    rightS = allNodes - node
                    leftSN = createTree(leftS)
                    rightSN = createTree(rightS)
                    if leftSN!= 0 and rightSN!= 0:
                        numberT+= leftSN*rightSN
                    elif leftSN== 0 and rightSN== 0:
                        numberT+=1
                    else:
                        numberT+= leftSN+rightSN
                return numberT
            else:
                return 0
        return createTree(n)
Solution().numTrees(3)
class Solution1:
    def numTrees(self, n: int) -> int:
        # Intuition

        # The problem can be solved in a dynamic programming way.

        # Given a sorted sequence 1 ... n, to construct a Binary Search Tree (BST) out of the sequence, 
        # we could enumerate each number i in the sequence, and use the number as the root, 
        # then, the subsequence 1 ... (i-1) on its left side would lay on the left branch of the root, 
        # and similarly the right subsequence (i+1) ... n lay on the right branch of the root. 
        # We then can construct the subtree from the subsequence recursively. 
        # Through the above approach, we could be assured that the BST that we construct are all unique, 
        # since they start from unique roots.

        #nodeIndex is from 1 to n
        if n>0:
            numberT = 0
            for node in range(1,n+1):
                leftS = node -1
                rightS = n - node
                leftSN = self.numTrees(leftS)
                rightSN = self.numTrees(rightS)
                if leftSN!= 0 and rightSN!= 0:
                    numberT+= leftSN*rightSN
                elif leftSN== 0 and rightSN== 0:
                    numberT+=1
                else:
                    numberT+= leftSN+rightSN
            return numberT
        else:
            return 0
class Solution2:
    def numTrees(self, n: int) -> int:
        # change Solution1 to DP solution.
        NumberN = [1,1]
        for i in range(2, n+1):
            for j in (0,i+1):
                NumberN[i] = NumberN[j]*NumberN[i-j-1]
        return NumberN[n]
            numberT = 0
            for node in range(1,n+1):
                leftS = node -1
                rightS = n - node
                leftSN = self.numTrees(leftS)
                rightSN = self.numTrees(rightS)
                if leftSN!= 0 and rightSN!= 0:
                    numberT+= leftSN*rightSN
                elif leftSN== 0 and rightSN== 0:
                    numberT+=1
                else:
                    numberT+= leftSN+rightSN
            return numberT
        else:
            return 0

