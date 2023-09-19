# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast = slow = head
        # If the number of nodes is less than 2, then LL can't have a cycle.
        if not fast or not fast.next:
            return False

        # Keep going through the list 
        # If at any point fast or fast.next is None, then LL is not cycllic.
        # If we reach a point where slow and fast are equal, then LL is cyclic.
        while fast.next:
            fast = fast.next.next
            slow = slow.next

            if not fast:
                return False
            
            if fast==slow:
                return True
        