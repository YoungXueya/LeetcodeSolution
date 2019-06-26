# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    # First reverse the latter half, then compare the head and the tail.
    # Need to figure out how to reverse an linked list problem 206
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow,fast=head,head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=None
        while slow:
            nxt=slow.next
            slow.next=temp
            temp=slow
            slow=nxt
        while temp and head:
            if temp.val==head.val:
                temp=temp.next
                head=head.next
            else:
                return False
        return True
            
