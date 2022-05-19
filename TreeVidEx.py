class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.designation = designation
        self.children = []
        self.parent = None

    def get_level(self):
        level = 0
        p = self
        while p.parent:
            level+=1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self, parameter, bound):
        spaces = self.get_level() * ' ' * 3
        prefix = spaces + "|__" if self.parent else ''
        level = self.get_level()

       #print(
        if parameter=="name":
            print(prefix + self.data)
        elif parameter=="designation":
            print(prefix + self.designation)
        else:
            print(prefix + self.data + " " + "("+self.designation+")")
        #    )


        if self.children and level<bound:
            for child in self.children:
                child.print_tree(parameter, bound)



def build_product_tree():
    root = TreeNode("CEO", "Norton")

    CTO = TreeNode("CTO", "Charlie")

    IH = TreeNode("Infrastructure Head", "Vince")
    IH.add_child(TreeNode("App Manager", "Alan"))
    IH.add_child(TreeNode("Cloud Manager", "David"))
    CTO.add_child(IH)

    AH = TreeNode("Application Head", "Aamir")
    CTO.add_child(AH)


    HH = TreeNode("HR Head", "Gels")
    HH.add_child(TreeNode("Recruitment Manager", "Peter"))
    HH.add_child(TreeNode("Policy Manager", "Waqas"))

    root.add_child(CTO)
    root.add_child(HH)



    return root

node = build_product_tree()
node.print_tree("name", 1)
