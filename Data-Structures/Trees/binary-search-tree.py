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

    def breath_first_search(self):
        binary_tree_array = []
        childrens_queue = [self.root]
        for node in childrens_queue:
            binary_tree_array.append(node.value)
            if node.left is not None:
                childrens_queue.append(node.left)
            if node.right is not None:
                childrens_queue.append(node.right)
                
        return binary_tree_array

    def breath_first_search_recursion(self, childrens_queue, binary_tree_array):
        if not childrens_queue:
            return binary_tree_array
        current_node = childrens_queue.pop(0)
        binary_tree_array.append(current_node.value)
        if current_node.left is not None:
            childrens_queue.append(current_node.left)
        if current_node.right is not None:
            childrens_queue.append(current_node.right)
                
        return self.breath_first_search_recursion(childrens_queue, binary_tree_array)
    
    def depth_first_search(self):
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
# tree.remove(170)

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

print("-----------------------------")

bfs_array = tree.breath_first_search()
bfs_array_recursion = tree.breath_first_search_recursion([tree.root], [])
print(f"Breath First Search -- Iterative Approach : {bfs_array}")
print(f"Breath First Search -- Recursive Approach : {bfs_array_recursion}")