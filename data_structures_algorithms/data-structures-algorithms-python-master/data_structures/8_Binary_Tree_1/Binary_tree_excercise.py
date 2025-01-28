# Add following methods to [BinarySearchTreeNode class]

#     1. find_min(): finds minimum element in entire binary tree
#     2. find_max(): finds maximum element in entire binary tree
#     3. calculate_sum(): calcualtes sum of all elements
#     4. post_order_traversal(): performs post order traversal of a binary tree
#     5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return # node already exist

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements
    

    # post order traversal example

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)
        
        return elements
        


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

def find_min(root):
    if root.left is None:
        return root.data
    return find_min(root.left)

def find_max(root):
    if root.right is None:
        return root.data
    return find_max(root.right)

def calculate_sum(root):
    if root is None:
        return 0
    return root.data + calculate_sum(root.left) + calculate_sum(root.right)


def print_tree(root, level=0):
    if root is None:
        return
    print_tree(root.right, level + 1)
    print(' ' * 4 * level + '->', root.data)
    print_tree(root.left, level + 1)

if __name__ == '__main__':
    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("print tree: ", print_tree(numbers_tree))
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())
    print("Post order traversal gives this sorted list:",numbers_tree.post_order_traversal())
    print("Sum of all numbers is:",calculate_sum(numbers_tree))
    print("Min number is:",find_min(numbers_tree))
    print("Max number is:",find_max(numbers_tree))
