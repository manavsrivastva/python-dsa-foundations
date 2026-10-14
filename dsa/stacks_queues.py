"""Stack is LIFO; queue is FIFO."""
from collections import deque


class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)  # amortized O(1)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._items[-1]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek at empty queue")
        return self._items[0]

    def is_empty(self):
        return not self._items

    def __len__(self):
        return len(self._items)


def stack_queue_examples():
    stack = Stack()
    stack.push("first")
    stack.push("second")
    print("Stack top:", stack.peek(), "| popped:", stack.pop())
    queue = Queue()
    queue.enqueue("first")
    queue.enqueue("second")
    print("Queue front:", queue.peek(), "| dequeued:", queue.dequeue())
