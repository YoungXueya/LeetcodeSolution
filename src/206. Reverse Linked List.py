# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#Iterative works better than recursive
class Solution:
    #Recursive
    def reverseList(self, head: ListNode) -> ListNode:
        return self.reverseCur(head,None)
    
    def reverseCur(self,head,newHead):
        if not head:
            return newHead
        next=head.next
        head.next=newHead
        return self.reverseCur(next,head)
        
        
    
    #Iterative
    def reverseList1(self, head: ListNode) -> ListNode:
        newHead=None
        while(head):
            next=head.next
            head.next=newHead
            newHead=head
            head=next
        return newHead
            
    
            
        
