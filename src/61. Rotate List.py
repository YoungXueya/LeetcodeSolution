# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Done with 3 pointers
    # End: current end, will point to current head
    # NewHead: currently points to the head, will point to the new head.
    # newEnd: will go to the new end, which next will be the new head.

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        newHead=ListNode(0)
        newHead.next=head
        end=newHead
        newEnd=newHead
        length=0
        while(end.next):
            end=end.next
            length+=1
        k=k%length
        for i in range(length-k):
            newEnd=newEnd.next
       
        end.next=newHead.next; 
        newHead.next=newEnd.next;
        newEnd.next=None;
        return newHead.next
        
            
