class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next

def insertAtHead(start,val):
    new_node = Node(val)
    new_node.next = start
    start = new_node
    return(start)

def insertList(start,lst):
    for item in lst:
        start = insertAtHead(start,item)
    return(start)

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

l1 = Node(0)
l1 = insertList(l1,[1,2,3,4])
print('Original List')
printList(l1)
print('Reversed List')
tail,head = reverseList(l1)
printList(head)
