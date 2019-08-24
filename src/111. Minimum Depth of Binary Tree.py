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
 # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root==None:
            return 0
        queue = deque([(root,1)])
        while queue:
            node,l = queue.popleft()
            if node.left is None and node.right is None:
                return l
            else:
                if node.left:
                    queue.append((node.left,l+1))
                if node.right:
                    queue.append((node.right,l+1))
        
