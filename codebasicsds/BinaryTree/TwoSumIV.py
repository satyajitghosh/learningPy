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

def TwoSumFour(root,value):

    l = set()
    def dfs(node):
        if not node: return False
        y = value - node.val
        if y in l:
            return True
        else:
            l.add(node.val)
        return dfs(node.left) or dfs(node.right)

    return(dfs(root))

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(TwoSumFour(t1,17))
