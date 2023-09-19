# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(p:ListNode,q:ListNode):
            temp = p.next
            p.next = q
            if temp:
                return(reverse(temp,p))  
            else:
                return(p) 
        
        if head:
            return reverse(head,None)  
        else:
            return None