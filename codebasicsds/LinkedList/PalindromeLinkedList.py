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

def isPalindrome(head):
    # Finding the middle element
    # Returns the left middle in case of twpo middles(list of even length)
    fast = head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    toReverse = slow.next
    tailReversed,headReversed = reverseList(toReverse)
    itr1 = head
    itr2 = headReversed

    isPalindrome = True

    while itr2:
        if itr1.val == itr2.val:
            print(f'l1={itr1.val},l2={itr2.val}')
            itr1 = itr1.next
            itr2 = itr2.next
        else:
            isPalindrome = False
            break

    return(isPalindrome)

l1 = Node(1)
l1 = insertList(l1,[4,3,4,1])
printList(l1)
print(isPalindrome(l1))

l2 = Node(1)
l2 = insertList(l2,[2,9,7])
printList(l2)
print(isPalindrome(l2))
