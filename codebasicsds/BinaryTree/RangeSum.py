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

def range_sum(node,low,high):
    if not node:
        return 0
    else:
        sum = 0
        if node.val >= low and node.val <=high:
            sum = sum + node.val
        sum += range_sum(node.left,low,high) + range_sum(node.right,low,high)
        return(sum)

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(range_sum(t1,8,9))
