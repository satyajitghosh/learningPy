import collections

class BSTNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

def add_child(head,val):
    if head.val == val:
        return
    elif val < head.val:
        if not head.left:
            head.left = BSTNode(val)
        else:
            add_child(head.left,val)
    else:
        if not head.right:
            head.right = BSTNode(val)
        else:
            add_child(head.right,val)

def add_list(head,lst):
    for item in lst:
        add_child(head,item)

def in_order_traversal(head):
    elements = []
    if head.left:
        elements = elements + in_order_traversal(head.left)
    elements.append(head.val)
    if head.right:
        elements = elements + in_order_traversal(head.right)
    return elements

def levelOrder(root):
    ## Note - Recursion is not required.
    ## Initial Queue length is calculated at each level.
    ## Only the elements of current level are popped.
    ## Children of the current level are appended to the right.
    ## Others are appended at the right. These are popped at the next iteration.

    queue = collections.deque()
    queue.append(root)
    full_list = []

    while queue:
        currSize = len(queue)
        currList = []

        while currSize > 0:
            currNode = queue.popleft()
            currList.append(currNode.val)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
            currSize = currSize - 1

        full_list.insert(0,currList)

    return(full_list)

print('-----------------------Test1------------------------------------------')
t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))
print(levelOrder(t1))
print('-----------------------Test2------------------------------------------')
