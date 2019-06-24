# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # Cleaver, 2-pass visit. pointer A len(A+B)=pointer B: len(B+A)
    # Same when the same part was subtract at the second pass
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA==None or headB==None:
            return None
        dummyA=headA
        dummyB=headB
        while headA!=headB:
            if headA==None:
                headA=dummyB
            else:
                headA=headA.next
            if headB==None:
                headB=dummyA
            else:
                headB=headB.next
        return headA
            
        
    def getIntersectionNode1(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        setA=set()
        while headA:
            setA.add(headA)
            headA=headA.next
        while headB:
            if headB in setA:
                return headB
            headB=headB.next
        return None
        
