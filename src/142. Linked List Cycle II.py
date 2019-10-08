# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # O(n) time, O(1) space
    # Floyd Algorithm
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast=head
        slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
            
        return slow
    
    # O(n) space, O(n) time
    def detectCycle(self, head: ListNode) -> ListNode:
        Set=set()
        while head:
            if head not in Set:
                Set.add(head)
                head=head.next
            else:
                return head
        return None
