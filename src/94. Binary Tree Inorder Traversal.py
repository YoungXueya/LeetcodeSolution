# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                node=stack.pop()
                ans.append(node.val)
                root=node.right
        return ans
                    
                
                
                
                
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        result=[]
        if(root!=None):
            self._add(root,result)
        return result
        
    def _add(self,root,result):
        
        if root.left!=None:
            self._add(root.left,result)
       
        result.append(root.val)    
       
        if root.right!=None:
            self._add(root.right,result)
        
        return result
    
        
        
