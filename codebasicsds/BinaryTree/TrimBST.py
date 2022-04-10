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

def trim_bst(node,low,high):
    if not node:
        return None
    if node.val < low:
        if node.right:
            return trim_bst(node.right,low,high)
        else:
            return None
    elif node.val > high:
        if node.left:
            return trim_bst(node.left,low,high)
        else:
            return None
    else:
        node.left = trim_bst(node.left,low,high)
        node.right = trim_bst(node.right,low,high)
    return node

t1=Node(3)
t1.left = Node(0)
t1.right = Node(4)
t1.left.right = Node(2)
t1.left.right.left = Node(1)

print(in_order_traversal(t1))
print(trim_bst(t1,1,3))
print(in_order_traversal(t1))
