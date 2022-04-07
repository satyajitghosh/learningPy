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

def tilt(root):
    if not root:
        return 0,0
    else:
        sumleft,tiltsumleft = tilt(root.left)
        sumright,tiltsumright = tilt(root.right)
        totalSum = sumleft+sumright+root.val
        root.val = abs(sumleft-sumright)
        tiltsum = (tiltsumleft+tiltsumright+root.val)
        return totalSum,tiltsum

t1=Node(4)
t1.left = Node(2)
t1.right = Node(9)
t1.left.left = Node(3)
t1.left.right = Node(5)
t1.right.right = Node(7)
print(in_order_traversal(t1))
sum,tiltsum = tilt(t1)
print(in_order_traversal(t1))
print(tiltsum)
