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

def pathSum(root,targetSum):

    paths = []

    def append_paths(path):
        paths.append(path)

    def build_paths(node,path):
        this_level_path = path.copy()
        this_level_path.append(node.val)
        if not node.left and not node.right:
            if sum(this_level_path)==targetSum:
                print(this_level_path)
                append_paths(this_level_path)
        if node.left:
            build_paths(node.left,this_level_path)
        if node.right:
            build_paths(node.right,this_level_path)

    build_paths(root,[])
    return(paths)

t1=Node(4)
t1.left = Node(2)
t1.right = Node(9)

print(in_order_traversal(t1))
print(pathSum(t1,6))
