class TreeNode():

    def __init__(self,data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        self.children.append(child)
        child.parent = self

    def get_level(self):
        level = 0
        while (self.parent):
            self = self.parent
            level += 1
        return(level)

    def print_tree(self):
        prefix = ""
        if self.get_level() > 0:
            prefix = " " * self.get_level() + "|__"
        print((prefix + self.data))
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cellphone")
    root.add_child(cellphone)
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    root.add_child(tv)
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.print_tree()
    tv.print_tree()
    print(tv.get_level())

if __name__ == '__main__':
    build_product_tree()
