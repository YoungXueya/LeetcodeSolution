# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            Node=TreeNode(t1.val+t2.val)
            Node.left=self.mergeTrees(t1.left,t2.left)
            Node.right=self.mergeTrees(t1.right,t2.right)
            return Node
        else:
            return t1 if t1 else t2
