# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        queue=deque()
        res=[]
        if not root:
            return 0
        queue.append(root)
        
        while queue:
            size=len(queue)
            for i in range(size):
                node=queue.popleft()
                res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        res=sorted(res)
        minABS=res[-1]-res[0]
        for i in range(len(res)-1):
            minABS=min(minABS,res[i+1]-res[i])
        return minABS
                
