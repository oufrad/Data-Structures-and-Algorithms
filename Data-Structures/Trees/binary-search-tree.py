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
        """
            There are three type of DFS algorithme. there is inOrder, PreOrder, PostOrder.  
            each one of them has it's own method and can be implemented in diffrent ways. 
            Here is exemples to how each of those Algorithms work :
                                        9
                                    4       20
                                  1   6   15   170

                    -- InOrder : [1, 4, 6, 9, 15, 20, 170]
                    -- PreOrder : [9, 4, 1, 6, 20, 15, 170]
                    -- PostOrder : [1, 6, 4, 15, 170, 20, 9]
        """
        pass
    
    def depth_first_search_in_order(self, starting_node, binary_tree_array):
        if starting_node.left is not None: 
            self.depth_first_search_in_order(starting_node.left, binary_tree_array)
        binary_tree_array.append(starting_node.value)
        if starting_node.right is not None: 
            self.depth_first_search_in_order(starting_node.right, binary_tree_array)

        return binary_tree_array

    def depth_first_search_pre_order(self, starting_node, binary_tree_array):
        binary_tree_array.append(starting_node.value)
        if starting_node.left is not None: 
            self.depth_first_search_pre_order(starting_node.left, binary_tree_array)
        if starting_node.right is not None: 
            self.depth_first_search_pre_order(starting_node.right, binary_tree_array)
        return binary_tree_array

    def depth_first_search_post_order(self, starting_node, binary_tree_array):
        if starting_node.left is not None: 
            self.depth_first_search_post_order(starting_node.left, binary_tree_array)
        if starting_node.right is not None: 
            self.depth_first_search_post_order(starting_node.right, binary_tree_array)
        binary_tree_array.append(starting_node.value)
        return binary_tree_array

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
print(f"Breath First Search -- Iterative Approach : {bfs_array}")

bfs_array_recursion = tree.breath_first_search_recursion([tree.root], [])
print(f"Breath First Search -- Recursive Approach : {bfs_array_recursion}")

dfs_array_in_order = tree.depth_first_search_in_order(tree.root, [])
print(f"Depth First Search : {dfs_array_in_order}")

dfs_array_pre_order = tree.depth_first_search_pre_order(tree.root, [])
print(f"Depth First Search : {dfs_array_pre_order}")

dfs_array_post_order = tree.depth_first_search_post_order(tree.root, [])
print(f"Depth First Search : {dfs_array_post_order}")