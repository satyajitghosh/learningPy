'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
'''

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

def isBalanced(root):
    if not root:
        return 0,True
    else:
        ls_depth,ls_balanced = isBalanced(root.left)
        rs_depth,rs_balanced = isBalanced(root.right)
        cur_depth = max(ls_depth,rs_depth) + 1
        if abs(rs_depth-ls_depth) <=1 and ls_balanced and rs_balanced:
            balanced = True
        else:
            balanced = False
    return cur_depth,balanced

print('-------------------Test1----------------')
t1 = Node(1)
t1.left = Node(2)
t1.right = Node(2)
t1.left.left = Node(3)
t1.left.right = Node(4)
t1.right.left = Node(4)
t1.right.right = Node(3)
print(in_order_traversal(t1))
depth,balanced = isBalanced(t1)
print(depth)
print(balanced)

print('-------------------Test2----------------')
t1 = Node(1)
t1.left = Node(2)
t1.left.left = Node(3)
print(in_order_traversal(t1))
print(in_order_traversal(t1))
depth,balanced = isBalanced(t1)
print(depth)
print(balanced)

print('-------------------Test3----------------')
t1 = Node(1)
t1.left = Node(2)
print(in_order_traversal(t1))
print(in_order_traversal(t1))
depth,balanced = isBalanced(t1)
print(depth)
print(balanced)
