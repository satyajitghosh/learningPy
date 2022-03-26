class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def insertAtHead(start,val):
    new_node = Node(val)
    new_node.next = start
    start = new_node
    return start

def insertList(start,lst):
    for item in lst:
        start = insertAtHead(start,item)
    return start

def printList(start):
    printstr = ''
    itr = start
    while itr:
        printstr = printstr + str(itr.val) + '-->'
        itr = itr.next
    printstr = printstr + 'END'
    print(printstr)

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

def reorderList(head):
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

print('-------------------First Test------------------')
l1 = Node(5)
l1 = insertList(l1,[4,3,2,1])
printList(l1)
reOrderedList = reorderList(l1)
printList(reOrderedList)
print('-------------------Second Test------------------')
l2 = Node(4)
l2 = insertList(l2,[3,2,1])
printList(l2)
reOrderedList = reorderList(l2)
printList(reOrderedList)
