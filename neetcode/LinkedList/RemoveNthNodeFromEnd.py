# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        
        if not head.next:
            return None
        
        slow = head
        fast = head
        
        i = 0

        # move slow ahead by n
        while i < n:
            fast = fast.next
            i = i+1

        # if fast has traversed n nodes and reached the end.
        # Clearly, the length of the list is n.
        # If the nth node from end has to be removed,
        # and the lenght is n.
        # that essentially means the first node must be removed.

        if not fast:
            return slow.next

        # now move both until fast reaches the end of the list.

        while fast.next:
            fast = fast.next
            slow = slow.next

        # This means that the fast ptr has moved ahead n times more than slow.
        # Or, the slow is behind fast by n.
        # Since fast is at the end, therefore, it means that the slow is n nodes behind the end.

        slow.next = slow.next.next
        
        return head

         