# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left=self.getDepth(root.left)
        right=self.getDepth(root.right)
        ldia=self.diameterOfBinaryTree(root.left)
        rdia=self.diameterOfBinaryTree(root.right)
        return max(left+right,ldia,rdia)
    
    def getDepth(self,root):
        if not root:
            return 0
        else:
            return max(self.getDepth(root.left),self.getDepth(root.right))+1
        
