# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        queue=deque()
        res=0
        if not root:
            return 0
        queue.append(dict({root:False}))
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                for key, value in node.items():
                    if value and not key.left and not key.right:
                        res+=key.val
                        continue
                    if key.left:
                        print(key.left)
                        queue.append(dict({key.left:True}))
                    if key.right:
                        queue.append(dict({key.right:False}))
        return res
        
