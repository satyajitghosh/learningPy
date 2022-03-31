class Node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

def in_order_traversal(head):
    elements = []
    if head.left:
        elements = elements + in_order_traversal(head.left)
    elements.append(head.val)
    if head.right:
        elements = elements + in_order_traversal(head.right)
    return elements

def sameTree(leftSubtree,rightSubTree):
    if not leftSubtree and not rightSubTree:
        return True
    elif leftSubtree and rightSubTree:
        return(leftSubtree.val == rightSubTree.val and sameTree(leftSubtree.left,rightSubTree.right) and sameTree(leftSubtree.right,rightSubTree.left))
    else:
        return False

def sameTreeWrapper(Tree):
    if not Tree:
        return True
    else:
        return sameTree(Tree.left,Tree.right)

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
t1.right.right = Node(3)
print(in_order_traversal(t1))
print(sameTreeWrapper(t1))
