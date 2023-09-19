
from collections import deque
class ListNode:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = None

head = ListNode(1,None)
head.next = ListNode(2,None)
head.next.next = ListNode(3,None)
head.next.next.next = ListNode(4,None)
head.next.next.next.next = ListNode(5,None)

q = deque()
itr = head
resultlist = ListNode()
resultptr = resultlist

while itr:
    q.append(itr.val)
    itr = itr.next

print(q)

while(len(q) > 1):
    resultptr.next = ListNode(q.popleft(),None)
    resultptr = resultptr.next
    resultptr.next = ListNode(q.pop(),None)
    resultptr = resultptr.next

if len(q) > 0:
    resultptr.next = ListNode(q.pop(),None)

resultlist = resultlist.next
print(resultlist.val)
print(resultlist.next.val)
print(resultlist.next.next.val)
print(resultlist.next.next.next.val)
print(resultlist.next.next.next.next.val)
