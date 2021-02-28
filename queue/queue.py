from collections import deque 
class Queue:
    def __init__(self):
        self.buffer = deque()
    def enqueue(self, data):
        # self.buffer.insert(0,data)
        self.buffer.appendleft(data)
    def dequeue(self):
        self.buffer.pop()
    def is_empty(self):
        return len(self.buffer) == 0
    def size(self):
        return len(self.buffer)
q = Queue()
q.enqueue({
    'company': 'ABC',
    'timestamp': '15 Apr, 11.01 AM',
    'price': 131.10
})
q.enqueue({
    'company': 'DEF',
    'timestamp': '15 Apr, 11.02 AM',
    'price': 133.10
})

print(q.buffer)
q.dequeue()
print(q.buffer)