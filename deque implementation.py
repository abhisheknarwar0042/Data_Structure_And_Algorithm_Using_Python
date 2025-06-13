class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


d = Deque()
d.addRear(1)      # deque: [1]
d.addRear(2)      # deque: [2, 1]
d.addFront(3)     # deque: [2, 1, 3]
print(d.removeRear())   # Output: 2
print(d.removeFront())  # Output: 3
print(d.size())         # Output: 1
print(d.isEmpty())       #false

