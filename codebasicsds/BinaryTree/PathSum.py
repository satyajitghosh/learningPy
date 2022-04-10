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

def path_sum(root,targetSum):
    ## This is very confusing.
    ## SOmetimes this does not work.
    ## IF i declared has_sum without global keyword in the first instance, then
    ## has_sum is declared in path_sum function's namespace, not in the global namespace.
    ## Thus, there would be no way (at least I dont know any) to modify has_sum.
    ## has _sum would still be accessible but not availbale for modification.
    global has_sum
    has_sum = False
    def set_has_sum(val):
        global has_sum
        has_sum = val
    def check_path_sum(node,sumThisFar):
        sumThisFar = sumThisFar + node.val
        if not node.left and not node.right:
            if sumThisFar == targetSum:
                set_has_sum(True)
        if node.left:
            check_path_sum(node.left,sumThisFar)
        if node.right:
            check_path_sum(node.right,sumThisFar)

    check_path_sum(root,0)
    return has_sum

t1=Node(4)
t1.left = Node(1)
t1.right = Node(2)

print(in_order_traversal(t1))
print(path_sum(t1,6))
