# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue=collections.deque([root])
        odd=True
        result=[]
        while queue:
            temp=[]
            num=len(queue)
            for i in range(num):
                t = queue.popleft()
                if t:
                    if odd:
                        temp.append(t.val)
                    elif not odd:
                        temp.insert(0,t.val)
                    queue+=[t.left,t.right]
            if(len(temp)>0):
                result.append(temp)
            odd=not odd
        return result
                
                
            

        
