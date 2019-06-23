# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(nums)
        
        
    def helper(self,num:List[int]):
        if(len(num)<=0):
            return None
        mid=int(len(num)/2)
        root=TreeNode(num[mid])
        root.left=self.helper(num[0:mid])
        root.right=self.helper(num[mid+1:len(num)])
        return root
        
