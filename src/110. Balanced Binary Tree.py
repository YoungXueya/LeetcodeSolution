# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Same logic as https://leetcode.com/problems/maximum-depth-of-binary-tree/
    # Just add comparation at each level.
    def isBalanced(self, root: TreeNode) -> bool:
        
        return self.get_height(root)!=-1
    
    
    def get_height(self,root):
        if not root:
            return 0
        left=self.get_height(root.left)
        right=self.get_height(root.right)
        if left==-1 or right==-1:
            return -1
        if abs(left-right)>1:
            return -1
        return max(left,right)+1
        
