class BinarySearchTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value, None, None)
        if self.root is None: 
            self.insert_root(new_node)
        current_node = self.root
        while True:
            if current_node.value == value:
                return
            elif current_node.value > value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    return
            else:
                if current_node.right is not None:
                    current_node = current_node.right
                else: 
                    current_node.right = new_node
                    return
        return None

    def insert_root(self, node):
        self.root = node
        return

    def lookup(self, value):
        if self.root is None: 
            return False
        current_node = self.root
        while current_node is not None:
            if current_node.value == value:
                return True
            elif current_node.value > value: 
                current_node = current_node.left
            else: 
                current_node = current_node.right
        return False

    def remove(self, value):
        pass


class Node():
    def __init__(self, value, right, left):
        self.value = value
        self.right = right
        self.left = left


tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.remove(170)

def traverse(node):
    if node is None:
        return None

    tree = {'value': node.value}
    tree['left'] = traverse(node.left)
    tree['right'] = traverse(node.right)

    return tree

print(traverse(tree.root))

#      9
#   4     20
# 1  6  15  170

print(tree.lookup(4))