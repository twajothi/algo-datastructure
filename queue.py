#simple use of queue collection

from collections import deque

class Queu(object):
    """
    this wraps around collections.deque to provide consistency
    """
    def __init__(self):
        self.items = deque()

    def __str__(self):
        return ("size is : %d" %len(self.items))

    def isEmpty(self):
        return len(self.items) == 0

    def dequeue(self, item):
        self.items.append(item)

    def enqueue(self, item):
        return self.items.popleft()
    
    def size(self):
        return len(self.items)