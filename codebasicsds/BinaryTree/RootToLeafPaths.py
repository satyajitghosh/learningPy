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

def root_to_leaf_path(root):

    paths = []

    def append_paths(path):
        paths.append(path)

    def build_paths(node,path):
        if not node.left and not node.right:
            path = path + str(node.val)
            print(path)
            append_paths(path)
        path = path + str(node.val) + '->'
        if node.left:
            build_paths(node.left,path)
        if node.right:
            build_paths(node.right,path)

    build_paths(root,"")
    return(paths)

t1=Node(4)
t1.left = Node(2)
t1.left.left = Node(1)
t1.left.right = Node(3)
t1.right = Node(9)
t1.right.left = Node(8)
t1.right.right = Node(12)

print(in_order_traversal(t1))
print(root_to_leaf_path(t1))
