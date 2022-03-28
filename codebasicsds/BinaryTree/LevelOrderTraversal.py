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

def levelOrder(root):

    values = []
    if not root:
        return None

    cur_lvl_queue = []
    cur_lvl_queue.extend(root)
    nxt_lvl_queue = []

    for item in cur_lvl_queue:
        print(f"Item value --> {item.val}")
        values.append(item.val)
        if item.left:
            nxt_lvl_queue.append(item.left)
        if item.right:
            nxt_lvl_queue.append(item.right)

    next_values = levelOrder(nxt_lvl_queue)
    if next_values != None:
        values.append(next_values)
    return values

t1 = BSTNode(12)
add_list(t1,[6,18,3,9,15,21])
print(in_order_traversal(t1))
print(levelOrder([t1]))
