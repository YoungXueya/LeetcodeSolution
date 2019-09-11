# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # Using stack to reverse the values.
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
    # A cheating answer, for there is no limit for int in python, we can add all values then 
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        val1=0
        val2=0
        while l1:
            val1=val1*10+l1.val
            l1=l1.next
        while l2:
            val2=val2*10+l2.val
            l2=l2.next
        val1=val1+val2
        head=ListNode(0)
        if val1==0:
            return head
        while val1:
            val1,mod=divmod(val1,10)
            temp=ListNode(mod)
            temp.next=head.next
            head.next=temp
        return head.next
        
