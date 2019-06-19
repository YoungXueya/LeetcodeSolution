# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue=collections.deque([root])
        res=[]
        
        while queue:
            print(res)
            length=len(queue)
            tempList=[]
            for i in range(0,length):
                temp=queue.popleft()
                if(temp is not None):                   
                    tempList.append(temp.val)
                    queue+=[temp.left,temp.right] 
            if len(tempList)==0:
                continue
            res.insert(0,tempList)
        return res
                
        

        
