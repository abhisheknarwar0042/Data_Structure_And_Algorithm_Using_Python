class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
q.enqueue(1)  # Queue: [1]
q.enqueue(2)  # Queue: [2, 1]
q.enqueue(3)  # Queue: [3, 2, 1]

print(q.dequeue())  # Output: 1
print(q.dequeue())  # Output: 2
print(q.size())     # Output: 1
