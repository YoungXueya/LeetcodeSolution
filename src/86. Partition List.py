# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        h1=left=ListNode(0)
        h2=right=ListNode(0)
        while head:
            if head.val<x:
                left.next=head
                left=left.next
            else:
                right.next=head
                right=right.next
            head=head.next
        right.next=None
        left.next=h2.next
        return h1.next
        
