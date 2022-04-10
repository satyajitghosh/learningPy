class Node:
    def __init__(self,val=None,left=None,right=None):
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

def kth_smallest(root,k):

    stack = []
    stack.append(root)
    lst = []
    node = root
    while stack and len(lst) < k:
        if stack[-1].left:
            node = stack[-1].left
            stack[-1].left = None
            stack.append(node)
        else:
            node = stack.pop()
            lst.append(node.val)
            if node.right:
                stack.append(node.right)
    return lst[-1]

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(kth_smallest(t1,7))
