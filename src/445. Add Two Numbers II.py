# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1=[]
        s2=[]
        carry=0
        while l1:
            s1.append(l1.val)
            l1=l1.next
        while l2:
            s2.append(l2.val)
            l2=l2.next
        # print(s1,s2)
        head=ListNode(0)
        while s1 or s2 or carry:
            val=0
            if s1:
                val+=s1.pop()
            if s2:
                val+=s2.pop()
            carry,val=divmod(val+carry,10)
            temp=ListNode(val)
            temp.next=head.next
            head.next=temp
        return head.next
        
