# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #interative
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res,stack=[],[]
        while stack or root:
            if root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            else:
                node=stack.pop()
                root=node.right
        return res
    
    
    #recursive
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        result=[]
        if root:
            self._helper(root,result)
        return result
    
    def _helper(self,root,result):
        if root:
            result.append(root.val)
            self._helper(root.left,result)
            self._helper(root.right,result)
        return result
        
