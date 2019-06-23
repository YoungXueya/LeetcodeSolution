# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Use two pointer to find a cycle.
    # O(n) time, O(1) space
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slower=head
        faster=head
        while faster and faster.next:
            slower=slower.next
            faster=faster.next.next
            if(faster==slower):
                return True   
        return False
    # O(n) space and time
    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        listSet=set()
        while head:
            if head==None:
                return False
            else:
                if head in listSet:
                    return True
                else:
                    listSet.add(head)
            head=head.next
        return False
            
        
