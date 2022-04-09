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

def min_abs_diff(node):
    lst = in_order_traversal(node)
    minval = lst[1]-lst[0]
    for i in range(1,len(lst)):
        if(lst[i]-lst[i-1]) < minval:
            minval = lst[i]-lst[i-1]
    return(minval)


t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(min_abs_diff(t1))
