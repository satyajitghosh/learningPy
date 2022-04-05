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

def mergeTree(t1,t2):
    if not t1 and not t2:
        return None
    elif not t1 and t2:
        return t2
    elif t1 and not t2:
        return t1
    else:
        new_node = Node((t1.val+t2.val))
        new_node.left = mergeTree(t1.left,t2.left)
        new_node.right = mergeTree(t1.right,t2.right)
        return new_node

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
print(in_order_traversal(t1))

t2 = Node(3)
t2.right = Node(4)
print(in_order_traversal(t2))

t3 = mergeTree(t1,t2)
print(in_order_traversal(t3))
