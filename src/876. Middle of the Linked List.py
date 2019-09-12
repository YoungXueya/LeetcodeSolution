# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Using a count to record the list is odd or even.
    def middleNode(self, head: ListNode) -> ListNode:
        count=0
        slow=head
        fast=head
        while fast.next and fast.next.next:
            slow=slow.next
            print("forward")
            if fast.next and not fast.next.next:
                count+=1
            if fast.next and fast.next.next:
                count+=2
            fast=fast.next.next
        if fast.next:
            count+=1
        if count%2==0:
            return slow
        else:
            return slow.next
        
