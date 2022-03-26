'''
Given the head of a linked list, rotate the list to the right by k places.
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

def rotateList(head,k):
    if not head or not head.next:
        return head

    # Traverse till the end and count the nodes

    itr = head
    ctr = 1
    while itr.next:
        ctr = ctr+1
        itr = itr.next

    # Connect the tail to the head.
    itr.next = head

    # Calculating the number of movements
    if k > ctr:
        x = k % ctr
    else:
        x = k
    m = ctr-x

    # Move ahead in the cycle m times.
    i = 1
    while i <= m:
        i = i+1
        itr = itr.next

    new_head = itr.next
    itr.next = None
    return(new_head)

print('-----------------------Test1-----------------------------')
l1 = Node(5)
l1 = insertList(l1,[4,3,2,1])
printList(l1)
x = rotateList(l1,2)
printList(x)
print('-----------------------Test2-----------------------------')
l1 = Node(2)
l1 = insertList(l1,[1,0])
printList(l1)
x = rotateList(l1,4)
printList(x)
