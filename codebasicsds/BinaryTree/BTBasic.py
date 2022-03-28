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

def search(head,val):
    if head.val == val:
        return True
    elif val < head.val:
        if head.left:
            search(head.left)
        else:
            return False
    else:
        if head.right:
            search(head.right)
        else:
            return False

def find_max(head):
    if head.right:
        find_max(head.right)
    else:
        return head.val

def find_min(head):
    if head.left:
        find_max(head.left)
    else:
        return head.val
# Concept
# If the node to delete doesnt have any children- easy peasy- just delete.
# If the node to delete has children - you have to decide -
# Which of these children will take it's place?
# If there is one child - the child will take the deleted parent's place.
# If there are two children - you have to decide which child will take it's place
# while preserving the integrity of the tree data structure.
# Two options
# Either it will be replaced by the max value of it's left subtree.
# Or, by the min value of it's right subtree

def delete(head,val):
    if val < head.val:
        if head.left:
            head.left = delete(head.left,val)
    elif val > head.val:
        if head.right:
            head.right = delete(head.right,val)
    else:
        if head.left is None and head.right is None:
            return None
        elif head.left is None:
            return head.right
        elif head.right is None:
            return head.left
        else:
            min = find_min(head.right)
            head.val = min
            head.right = delete(head.right,min)
            return head

t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))
