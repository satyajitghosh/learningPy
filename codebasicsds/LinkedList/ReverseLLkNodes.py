'''
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.
'''
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

def reverseLLkNodes(head,k):
    itrO = head
    itrI = head
    resultHead = None
    resultitr = None

    while itrO:
        i = 1
        toReverse = None
        itrI=itrO
        while itrI.next and i<k:
            itrI = itrI.next
            i = i + 1
        if i==k:
            toReverse=itrO
            nextpart=itrI.next
            itrI.next=None
            tailReversed,headReversed = reverseList(itrO)
            itrO=nextpart
            if not resultHead:
                resultHead = headReversed
                resultitr = resultHead
                while resultitr.next:
                    resultitr = resultitr.next
            else:
                resultitr.next = headReversed
                while resultitr.next:
                    resultitr = resultitr.next
        else:
            if not resultHead:
                resultHead = itrO
                resultitr = itrO
                while resultitr.next:
                    resultitr = resultitr.next
            else:
                resultitr.next = itrO
                while resultitr.next:
                    resultitr = resultitr.next
            itrO = itrI.next
    return(resultHead)

print('-----------------------Test1-----------------------------')
l1 = Node(5)
l1 = insertList(l1,[4,3,2,1])
printList(l1)
x = reverseLLkNodes(l1,2)
printList(x)

print('-----------------------Test2-----------------------------')
l1 = Node(5)
l1 = insertList(l1,[4,3,2,1])
printList(l1)
x = reverseLLkNodes(l1,3)
printList(x)
