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

def minval(node):
    if node.left:
        return minval(node.left)
    else:
        return node.val

def delete_node(node,key):
    if node is None:
        return None
    if key < node.val:
        if node.left:
            node.left = delete_node(node.left,key)
    elif key > node.val:
        if node.right:
            node.right = delete_node(node.right,key)
    elif key == node.val:
        if not node.left and not node.right:
            return None
        elif node.left and not node.right:
            return node.left
        elif not node.left and node.right:
            return node.right
        else:
            minvalue = minval(node.right)
            node.val = minvalue
            node.right = delete_node(node.right,minvalue)
    return node

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(delete_node(t1,9))
print(in_order_traversal(t1))

t2=Node(5)
t2.left = Node(3)
t2.left.left = Node(2)
t2.left.right = Node(4)
t2.right = Node(6)
t2.right.right = Node(7)
print(in_order_traversal(t2))
print(delete_node(t2,75))
print(in_order_traversal(t2))

t3=Node(5)
t3.left = Node(3)
t3.left.left = Node(2)
t3.left.right = Node(4)
t3.right = Node(6)
t3.right.right = Node(7)
print(in_order_traversal(t3))
print(delete_node(t3,3))
print(in_order_traversal(t3))
