# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        while root or stack:
            if root:
                result.append(root.val)
                print(result)
                stack.append(root)
                root=root.right
            else:
                node=stack.pop()
                root=node.left
        
        return result[::-1]
                
    #iterative
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        result=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            result.insert(0,node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return result
    
                
                
    #recursive
    def postorderTraversal1(self, root: TreeNode) -> List[int]:
        result=[]
        if root:
            self._helper(root,result)
        return result
        
    
    def _helper(self,root,result):
        if root:
            self._helper(root.left,result)
            self._helper(root.right,result)
            result.append(root.val)
        return result
        
