# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack=[]
        while True:
            while root:
                stack.append(root)
                root=root.left
            node=stack.pop()
            k-=1
            if not k:
                return node.val
            root=node.right
        
        
    def count(self,root):
        if not root:
            return 0
        return 1+self.count(root.left)+self.count(root.right)
    def kthSmallest1(self, root: TreeNode, k: int) -> int:
        stack=[]
        result=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            result.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        print("Finished")
        result.sort()
        return result[k-1]
        
