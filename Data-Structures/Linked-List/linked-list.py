class LinkedList():
    def __init__(self, head_value):
        self.head = Node(head_value, None)
        self.tail = self.head
        self.length = 1

    def convert_to_array(self):     # O(n)
        linked_array = []
        current_node = self.head
        while current_node is not None: 
            linked_array.append(current_node.value)
            current_node = current_node.next
        return linked_array

    def append(self, value):    # O(1)
        new_node = Node(value, None)
        if self.tail == self.head:
            self.head.next = new_node
            self.tail = new_node
        else: 
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):   # O(1)
        new_node = Node(value, self.head)
        self.head = new_node
        self.length += 1

    def insert(self, index, value):     # O(n)
        current_index = 0
        current_node = self.head 
        if index <= 0: 
            self.prepend(value)
            self.length += 1
            return
        elif index >= self.length:
            self.append(value)
            self.length += 1
            return
        while current_node is not None:
            if current_index == index - 1:
                new_node = Node(value, current_node.next)
                current_node.next = new_node
                self.length += 1
                return
            current_node = current_node.next
            current_index += 1

    def remove(self, index):        # O(n)
        current_index = 0
        current_node = self.head
        if index <= 0: 
            self.head = self.head.next
            self.length -= 1
            return
        while current_node is not None: 
            if current_index == index - 1 and current_index <= self.length:
                current_node.next = current_node.next.next
                self.length -= 1
                return
            current_node = current_node.next
            current_index += 1
            
    def reverse(self):          # O(n)
        if self.head.next is None: 
            return  self.head
        current_node = self.head
        previous_node = None
        next_node = self.head.next
        self.tail = self.head
        current_node.next = previous_node
        while next_node is not None:
            previous_node = current_node
            current_node = next_node
            next_node = next_node.next
            current_node.next = previous_node
        self.head = current_node

    # def travers_to_index(self, index):
    #     current_node = self.head
    #     while current_node is not None: 
    #         if current_index == index - 1:
    #             return current_node
    #         current_node = current_node.next
    #         current_index += 1
        
class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next
    

linked_list = LinkedList(19)
linked_list.append("Hellooo")
linked_list.append("My")
linked_list.append("Name is ")

linked_list.prepend("Hi")
print(linked_list.convert_to_array())

linked_list.insert(2,"Lelouch")

print(linked_list.convert_to_array())

linked_list.remove(3)
print(linked_list.convert_to_array())

linked_list.reverse()

print(linked_list.convert_to_array())