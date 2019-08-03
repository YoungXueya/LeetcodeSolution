# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #Recursive more easy to understand
    def isValidBST(self, root: TreeNode) -> bool:
        if root:
            return self.compare(root,sys.maxsize,-sys.maxsize-1)
        else:
            return True
    
    def compare(self, root,max,min):
        if not root:
            return True
        if(root.val>=max or root.val<=min):
            return False
        return (self.compare(root.left,root.val,min) and self.compare(root.right,max,root.val) )
    
    #Iteractive
    def isValidBST1(self, root: TreeNode) -> bool:
        stack=[]
        pre=None
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                node=stack.pop()
                if(pre and (pre.val>=node.val)):
                    return False
                pre=node
                root=node.right
        return True
        
