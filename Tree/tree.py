class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level =0;
        p= self.parent;
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '  ' * self.get_level() * 2;
        prefix = spaces+ '|__' if self.parent else ""
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)    
    mobile = TreeNode("Mobile")
    root.add_child(mobile)    

    laptop.add_child(TreeNode("Dell"))
    mobile.add_child(TreeNode("Nokia"))
    return root;

if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()

