# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        dic={}
        return self.subRob(root,dic)
    # There are two kinds of senario:
    # One is rob the root, another is  not rob the root.
    # If rob the root, Then only can rob its grandson nodes.
    # Use dic to track the calculated nodes maximum value.
    def subRob(self,root,dic):
        if not root:
            return 0
        if root in dic:
            return dic[root]
        
        val=0
        if root.left:
            val+=self.subRob(root.left.left,dic)+self.subRob(root.left.right,dic)
        if root.right:
            val+=self.subRob(root.right.left,dic)+self.subRob(root.right.right,dic)
        
        val=max(val+root.val,self.subRob(root.left,dic)+self.subRob(root.right,dic))
        dic[root]=val
        return val
            
        
