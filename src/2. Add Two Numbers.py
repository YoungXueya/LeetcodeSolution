# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        val=0
        dummy=cur=ListNode(0)
        
        while l1 or l2 or carry:
            val=0
            if l1:
                val+=l1.val
                l1=l1.next
            if l2:
                val+=l2.val
                l2=l2.next
            # print(val)
            carry,val=divmod(val+carry,10)
            cur.next=ListNode(val)
           # print(cur.val)
            cur=cur.next
        return dummy.next
            
            
