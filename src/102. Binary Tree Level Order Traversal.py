# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        queue=collections.deque([root])
        while queue:
            length=len(queue)
            temp=[]
            for i in range(length):
                cur=queue.popleft()
                if cur:
                    temp.append(cur.val)
                    queue+=[cur.left,cur.right]
            if len(temp)>0:
                res.append(temp)
            
        return res

        
