from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self, data):
        self.container.append(data)
    def pop(self):
        self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container) == 0
    def size(self):
        return len(self.container)

s = Stack()
s.push(5)
s.push(9)
s.push(7)
s.peek()
s.pop()
s.is_empty()
s.size()