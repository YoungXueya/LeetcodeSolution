# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy=ListNode(0)
        dummy.next=head
        if head==None:
            return head
        
        while head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return dummy.next
        
        
