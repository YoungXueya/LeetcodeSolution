"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        self.helper(root,res)
        return res
    
    def helper(self,root,res):
        if root:
            res.append(root.val)
            for child in root.children:
                self.helper(child,res)
        
        
