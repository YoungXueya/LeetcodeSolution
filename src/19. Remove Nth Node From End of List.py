# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length=0
        temp=head
        newHead=ListNode(0)
        newHead.next=head
        while temp:
            temp=temp.next
            length+=1
        # If there is only one element in the linked list
        if length==1:
            return None
        # If the one needed to be removed is the first one,just return the head.next
        if length-n==0:
            return head.next
        
        for i in range(length-n-1):
            head=head.next        
        head.next=head.next.next
        return newHead.next
        
     # One pass
     def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        newHead=ListNode(0)
        slow=ListNode(0)
        newHead.next=head 
        fast=head
        slow.next=head
        for i in range(n):
            fast=fast.next
        if not fast:
            return head.next
        while fast:
            fast=fast.next
            slow=slow.next
        if slow.next:
            slow.next=slow.next.next            
        return newHead.next
        
