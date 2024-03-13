class Queue():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def convert_to_array(self):
        current_node = self.head
        queue_array = []
        while current_node is not None:
            queue_array.append(current_node.value)
            current_node = current_node.next
        return queue_array
    
    def peek_front(self):
        return self.head.value
    
    def peek_back(self):
        return self.tail.value

    def enqueue(self, value):
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None
        if self.head.next is None: 
            self.head = None
            self.tail = None
            return None
        self.head = self.head.next
        self.length -= 1
        
class Node():
    def __init__(self, value, next):
        self.value = value
        self.next = next

queue = Queue()

queue.enqueue("Uvogin")
queue.enqueue("Chrollo Lucilfer")
queue.enqueue("Hisoka Morow")
queue.enqueue("Feitan")
queue.enqueue("Nobunaga Hazama")
queue.enqueue("Phinks")

print(f"Head : {queue.peek_front()}")
print(f"Tail : {queue.peek_back()}")

queue_array = queue.convert_to_array()
print(queue_array)

queue.dequeue()
queue.dequeue()

queue_array = queue.convert_to_array()
print(queue_array)