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

def invertTree(root):
    if not root:
        return None
    if root.left and not root.right:
        root.right = root.left
        root.left = None
        invertTree(root.right)
    if root.right and not root.left:
        root.left = root.right
        root.right = None
        invertTree(root.left)
    if root.left and root.right:
        temp = root.left
        root.left = root.right
        root.right = temp
        invertTree(root.left)
        invertTree(root.right)


t1=Node(4)
t1.left = Node(2)
t1.right = Node(9)
t1.left.left = Node(3)
t1.left.right = Node(5)
t1.right.right = Node(7)
t1.right.left = Node(8)
t1.right.right = Node(7)
print(in_order_traversal(t1))
invertTree(t1)
print(in_order_traversal(t1))
