class Array():
    def __init__(self, length):
        self.lenght = length
        self.items = [0] * length

    def to_string(self):    # O(n)
        return ' -> '.join([str(item) for item in self.items])

    def get_item(self, index):  # O(1)
        return self.items[index]

    def set_item(self, index, item):    # O(1)
        self.items[index] = item

    def insert(self, index, item):      # O(n)
        if self.lenght > index:
            for i in range(self.lenght - 2, index - 1, -1):
                self.items[i + 1] = self.items[i]
            self.items[index] = item
        else: 
            print(f"Array is of size: {self.lenght}")

    def search(self, searched_item):    # O(n)
        for item in self.items:
            if searched_item == item:
                return True
        return False

    def pop(self):      # O(1)
        self.items[self.lenght - 1] = 0 

    def remove(self, index):        # O(n)
        if self.lenght > index:
            for i in range(index, self.lenght - 1):
                self.items[i] = self.items[i + 1]
        else:
            print(f"Array is of size: {self.lenght}")


array = Array(10)

array.set_item(4, 19)
array.set_item(1, 'hi')
array.set_item(7, 'Hello')
array.set_item(6, 7)

# array.remove(4)
print(array.to_string())

# array.remove(7)
array.insert(2, 'hisoka')
array.insert(8, 'Lelouch')

print(array.to_string())