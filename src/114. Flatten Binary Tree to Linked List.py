# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # root.left.right.right=root.right
        # if left
        #   root.right=root.left
        # root.left=None
        temp=None
        while root:
            if root.left and root.right:
                temp=root.left
                while temp.right:
                    temp=temp.right
                temp.right=root.right
            if root.left:
                root.right=root.left
            root.left=None
            root=root.right
            
            
        
