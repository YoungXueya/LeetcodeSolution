# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import collections
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        stack=collections.deque()
        res=[]
        count=0
        while head:
            while stack and stack[-1][0]<head.val:
                val,index=stack.pop()
                while len(res)<=index:
                    res.append(0)
                res[index]=head.val
            stack.append([head.val,count])
            head=head.next
            count+=1
        while len(res)<=count-1:
            res.append(0)
        return res
                
        
