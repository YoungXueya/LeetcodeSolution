# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res=[]
        path=[root.val]
        self.helper(root,path,sum-root.val,res)
        return res
    
    def helper(self,root,path,sum,res):
        # print(root.val,path)
        if not root.left and not root.right and sum==0:
            res.append(path)
            return 
        if root.left:
            # print(curPath)
            self.helper(root.left,path+[root.left.val],sum-root.left.val,res)
        if root.right:
            self.helper(root.right,path+[root.right.val],sum-root.right.val,res)
        
