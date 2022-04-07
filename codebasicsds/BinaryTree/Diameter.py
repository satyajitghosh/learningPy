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

def diameter(root):

    if not root:
        node_depth = 0
        node_diameter = 0
        return node_depth,node_diameter

    else:
        left_depth,left_diameter = diameter(root.left)
        right_depth,right_diameter = diameter(root.right)
        node_depth = max(left_depth,right_depth) + 1
        node_diameter = max(left_diameter,right_diameter,(left_depth+right_depth))
        return node_depth,node_diameter

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
print(diameter(t1))

t2 = Node(3)
t2.right = Node(4)
t2.left = Node(6)
print(diameter(t2))

t3=Node(5)
t3.left = Node(6)
t3.right = Node(19)
t3.left.left = Node(7)
t3.left.right = Node(10)
t3.left.right.right = Node(12)
t3.left.right.right.right = Node(8)
t3.left.left.left = Node(8)
t3.left.left.left.left = Node(27)

print(diameter(t3))
