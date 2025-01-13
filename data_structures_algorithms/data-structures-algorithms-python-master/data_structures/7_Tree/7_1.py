# 1. Below is the management hierarchy of a company.

#     ![ss](management_both.PNG)

# Extent [tree class](https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/7_Tree/7_tree.py) built in our
# main tutorial so that it takes **name** and **designation** in data part of TreeNode class.
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree. As shown below,

#    ![](all_trees.png)

# Here is how your main function should will look like,
# ```
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy
# ```

class TreeNode:
    def __init__(self, data, designation):
        self.data = data
        self.children = []
        self.parent = None
        self.designation = designation

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self, printmode="name"):

        if printmode == "name":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_tree(printmode)
        elif printmode == "designation":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.designation)
            if self.children:
                for child in self.children:
                    child.print_tree(printmode)
        elif printmode == "both":
            spaces = ' ' * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.data + " (" + self.designation + ")")
            if self.children:
                for child in self.children:
                    child.print_tree(printmode)
        else:
            print("Invalid print mode. Use 'name', 'designation' or 'both'")

    

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    root.print_tree()


def build_management_tree():
    # CTO Hierarchy
    infra_head = TreeNode("Vishwa","Infrastructure Head")
    infra_head.add_child(TreeNode("Dhaval","Cloud Manager"))
    infra_head.add_child(TreeNode("Abhijit", "App Manager"))

    cto = TreeNode("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(TreeNode("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = TreeNode("Gels","HR Head")

    hr_head.add_child(TreeNode("Peter","Recruitment Manager"))
    hr_head.add_child(TreeNode("Waqas", "Policy Manager"))

    ceo = TreeNode("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo

root_node = build_management_tree()

root_node.print_tree("name")
print("")
root_node.print_tree("designation")
print("")
root_node.print_tree("both")
