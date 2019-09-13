# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        stack=[]
        stack.append(root)
        res=0
        while stack:
            temp=stack.pop()
            # print(temp.val)
            if temp.val<=R and temp.val>=L:
                if temp.left:
                    stack.append(temp.left)
                if temp.right:
                    stack.append(temp.right)
                res+=temp.val
            elif temp.val<L:
                if temp.right:
                    stack.append(temp.right)
            elif temp.val>R:
                if temp.left:
                    stack.append(temp.left)
        return res
