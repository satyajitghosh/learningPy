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


def maxDepth(root):
    if not root:
        return 0
    else:
        ls_depth = maxDepth(root.left)
        rs_depth = maxDepth(root.right)
        return(max(ls_depth,rs_depth)+1)

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
t1.right.right = Node(3)
print(in_order_traversal(t1))
print(maxDepth(t1))

print('-------------------Test2----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
print(in_order_traversal(t1))
print(maxDepth(t1))

print('-------------------Test3----------------')
t1 = Node(1)
t1.left = Node(2)
print(in_order_traversal(t1))
print(maxDepth(t1))
