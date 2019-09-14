# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        stack=[]
        if root:
            stack.append([root,sum])
        while stack:
            temp,value=stack.pop()
            if not temp.left and not temp.right and value-temp.val==0:
                return True
            if temp.left:
                stack.append([temp.left,value-temp.val])
            if temp.right:
                stack.append([temp.right,value-temp.val])
        return False
        
