# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        class Result:

            def __init__(self):
                self.result = None
                self.pos = None
            def append(self,ln:ListNode):
                if not self.result:
                    self.result = ln
                    self.pos = self.result
                else:
                    self.pos.next = ln
                    self.pos = self.pos.next
        
        rs = Result()

        while list1 and list2:
            if list1.val < list2.val:
                rs.append(ListNode(list1.val,None))
                list1 = list1.next
            else:
                rs.append(ListNode(list2.val,None))                
                list2 = list2.next
        
        if list1:
            rs.append(list1)
        if list2:
            rs.append(list2)

        return rs.result
