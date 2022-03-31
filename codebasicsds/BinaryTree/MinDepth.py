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


def minDepth(root):
    if not root:
        return 0
    else:
        ls_depth = minDepth(root.left)
        rs_depth = minDepth(root.right)
        if ls_depth==0 and rs_depth==0:
            return 1
        elif ls_depth==0:
            return (rs_depth+1)
        elif rs_depth==0:
            return (ls_depth+1)
        else:
            return(min(ls_depth,rs_depth)+1)

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
t1.right.right = Node(3)
print(in_order_traversal(t1))
print(minDepth(t1))

print('-------------------Test2----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
print(in_order_traversal(t1))
print(minDepth(t1))

print('-------------------Test3----------------')
t1 = Node(1)
t1.left = Node(2)
print(in_order_traversal(t1))
print(minDepth(t1))

print('-------------------Test3----------------')
t1 = Node(2)
t1.right = Node(3)
t1.right.right = Node(4)
t1.right.right.right = Node(5)
t1.right.right.right.right = Node(6)
print(in_order_traversal(t1))
print(minDepth(t1))
