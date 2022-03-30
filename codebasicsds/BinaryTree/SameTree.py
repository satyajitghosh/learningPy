import collections

class BSTNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None

def add_child(head,val):
    if head.val == val:
        return
    elif val < head.val:
        if not head.left:
            head.left = BSTNode(val)
        else:
            add_child(head.left,val)
    else:
        if not head.right:
            head.right = BSTNode(val)
        else:
            add_child(head.right,val)

def add_list(head,lst):
    for item in lst:
        add_child(head,item)

def in_order_traversal(head):
    elements = []
    if head.left:
        elements = elements + in_order_traversal(head.left)
    elements.append(head.val)
    if head.right:
        elements = elements + in_order_traversal(head.right)
    return elements

def sameTree(t1,t2):
    # Idea is to check if left subtree is same, right subtree is same and the data is same.
    # If the tree is structurally different - left child present/right absent or vice versa - False
    if (t1.left and not t2.left) or (not t1.left and t2.left) or (t1.right and not t2.right) or (not t1.right and t2.right):
        return False
    # no children - check if values match
    elif (not t1.left and not t1.right and not t2.left and not t2.right):
        return (t1.val==t2.val)
    # only left child exists -
    elif (t1.left and t2.left) and (not t1.right and not t2.right):
        return(t1.val==t2.val and sameTree(t1.left,t2.left))
    # only right child exists -
    elif (t1.right and t2.right) and (not t1.left and not t2.left):
        return(t1.val==t2.val and sameTree(t1.right,t2.right))
    # Both trees have both children and both subtrees match - True
    elif (t1.left and t2.left and t2.left and t2.right):
        return(t1.val==t2.val and sameTree(t1.left,t2.left) and sameTree(t1.right,t2.right))
    else:
        return False

print('-----------------------Test1------------------------------------------')
t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))


t2 = BSTNode(12)
add_list(t2,[6,18,3,9,15,21])
print(in_order_traversal(t2))

print('Checking -')
print(sameTree(t1,t2))

print('-----------------------Test2------------------------------------------')

t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))


t2 = BSTNode(12)
add_list(t2,[6,18,3,9,15,23])
print(in_order_traversal(t2))

print('Checking -')
print(sameTree(t1,t2))

print('-----------------------Test3------------------------------------------')

t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))


t2 = BSTNode(12)
add_list(t2,[6,18,3,9])
print(in_order_traversal(t2))

print('Checking -')
print(sameTree(t1,t2))
