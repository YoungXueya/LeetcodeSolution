# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=0
        stack=[]
        gpSet=set()
        if not root:
            return 0
        stack.append((root,None,None))
        while stack:
            root,parent,gp=stack.pop()
            if gp and gp.val%2==0:
                
                res+=root.val
                    
                    
            if root.left:
                stack.append((root.left,root,parent))
            if root.right:
                stack.append((root.right,root,parent))
        return res

        
