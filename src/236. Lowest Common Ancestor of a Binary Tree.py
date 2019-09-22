# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Logic of this problem is that lCA only are not empty when there is one target in its children .
    # If the left and right are both not empty, two target are in the left and right children.
    # At the original root, if left is None, then two targets must in the right children.
    # At the lower layer, if left and right are None, then return None.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root :
            return None
        if root==q or root == p:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left if left else right
        
