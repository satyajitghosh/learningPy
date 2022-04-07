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

def searchBST(root,value):
    if not root:
        return None
    elif root.val == value:
        return root
    elif value < root.val:
        if root.left:
            return searchBST(root.left,value)
        else:
            return None
    elif value > root.val:
        if root.right:
            return searchBST(root.right,value)
        else:
            return None

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
t2 = searchBST(t1,9)
print(in_order_traversal(t2))
