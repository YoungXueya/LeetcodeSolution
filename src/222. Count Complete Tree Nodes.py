# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
       
        if not root:
            return 0
        if self.getDepth(root.left)==self.getDepth(root.right):
            return pow(2,self.getDepth(root.left))+self.countNodes(root.right)
        else:
            return pow(2,self.getDepth(root.right))+self.countNodes(root.left)
        
    def getDepth(self,root):
            if not root:
                return 0
            else:
                return 1+self.getDepth(root.left)     
