# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # A iterative way, queue+BFS
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        queue=collections.deque([root.left,root.right])
        while queue:
            left,right=queue.popleft(),queue.popleft()
            if not left and not right:
                
                continue
            if not left or not right:
                return False
            if left.val==right.val:
                queue+=[left.right,right.left,left.left,right.right]                
            else:
                return False
        return True
            
          
    
    # A recursive way    
    def isSymmetric(self, root: TreeNode) -> bool:
        if root==None:
            return True
        return self.isMirror(root.left,root.right)
        
        
    def isMirror(self,left,right):
            if left==None and right==None:
                return True
            if left==None or right==None:
                return False
            if(left.val==right.val):
                return self.isMirror(left.right,right.left) and self.isMirror(left.left,right.right)
            else:
                return False
        
