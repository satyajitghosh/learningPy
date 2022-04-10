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

def kth_smallest(root1,root2):


    lst1 = in_order_traversal(root1)
    lst2 = in_order_traversal(root2)

    lst = []

    while lst1 or lst2:
        if lst1 and lst2:
            if lst1[0] < lst2[0]:
                lst.append(lst1.pop(0))
            else:
                lst.append(lst2.pop(0))
        elif lst1:
            lst.append(lst1.pop(0))
        elif lst2:
            lst.append(lst2.pop(0))

    return lst

t1 = Node(2)
t1.left = Node(1)
print(in_order_traversal(t1))

t2 = Node(3)
t2.right = Node(4)
print(in_order_traversal(t2))

print(kth_smallest(t1,t2))
