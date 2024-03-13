class Stack():
    def __init__(self):
        self.head = None
    
    def convert_to_array(self):
        current_node = self.head
        stack_array = []
        while current_node is not None:
            stack_array.append(current_node.value)
            current_node = current_node.next
        return stack_array

    def peek(self):
        return self.head

    def push(self, value):
        if self.is_empty():
            self.head = Node(value, None)
        else:
            new_node = Node(value, self.head)
            self.head = new_node

    def pop(self):
        if self.is_empty():
            self.head = None
        else:
            self.head = self.head.next

    def is_empty(self):
        if self.head is None: 
            return True
        else: 
            return False

class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next


stack = Stack()
stack.push("Gon freecss")
stack.push("killua zoldyck")
stack.push("Biscuit Krueger")
stack_array = stack.convert_to_array()
print(stack_array)

stack.pop()
stack_array = stack.convert_to_array()
print(stack_array)
