# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Remember this is a binary search Tree 
    # Left<root<right
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        stack=[]
        if root:
            stack.append(root)
        else:
            return None
        while stack:
            temp=stack.pop()
            if temp.val==val:
                return temp
            if temp.left and val<temp.val:
                stack.append(temp.left)
            if temp.right and val>temp.val:

                stack.append(temp.right)
        return None
        
