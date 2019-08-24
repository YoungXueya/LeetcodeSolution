# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if root==None:
            return 0
        
        if not root.right:
            return 1+self.minDepth(root.left)
        elif not root.left:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        
        
