# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        queue=collections.deque()
        if not s:
            return False
        queue.append(s)
        while queue:
            node=queue.popleft()
            if self.isSameTree(node,t):
                return True
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return False
            
    
    def isSameTree(self, p ,q) :
        if p==None or q==None:
            return p==q
        if p.val==q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        return False
