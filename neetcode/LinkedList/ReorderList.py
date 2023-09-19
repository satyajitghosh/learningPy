# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseList(itr):
            if not itr.next:
                head = itr
                return itr,head
            else:
                pick = itr
                itr = itr.next
                pick.next = None
                rev,head = reverseList(itr)
                rev.next = pick
                rev = rev.next
                return rev,head
        
        if not head or not head.next:
            return None
        
        fast = head
        slow = head

        # this provides the mid left
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        
        #we go to mid right - that is where reversal needs to start.
        toReverse = slow.next
        #separate the left list from the right
        slow.next = None

        tailReversed,headReversed = reverseList(toReverse)
        itr1 = head
        itr2 = headReversed
        resultHead = None
        resultitr = None
        while itr1:
            pick1 = itr1
            itr1=itr1.next
            pick1.next = None

            if not resultHead:
                resultHead = pick1
                resultitr = resultHead
            else:
                resultitr.next = pick1
                resultitr = resultitr.next

            if itr2:
                pick2 = itr2
                itr2 = itr2.next
                pick2.next = None
                resultitr.next = pick2
                resultitr = resultitr.next
        
        return(resultHead)