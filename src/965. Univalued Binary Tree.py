# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        value=root.val
        stack=[]
        stack.append(root)
        while stack:
            root=stack.pop()
            if value!=root.val:
                return False
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)
        return True
        
