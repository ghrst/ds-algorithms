'''
Problem: Use Python lists to implement a queue. For more information about queue ADT refer to:
https://en.wikipedia.org/wiki/Queue_(abstract_data_type)
'''


class QueueEmpty(Exception):
    pass


# Caution: This implementation does not shrink the memory of the underlying list. This will result in an O(m)
#          memory complexity where m is the maximum number of enqueue operations during lifetime of the queue
class ListQueue:
    DEFAULT_CAPACITY = 10
    def __init__(self):
        self._data = [None] * ListQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise QueueEmpty('Queue is empty!')
        return self._data[self._front]
    
    def _resize(self, capacity):
        old = self._data
        self._data = [None] * capacity
        start = self._front
        for i in range(self._size):
            self._data[i] = old[start]
            start = (start + 1) % len(old)
        self._front = 0
        
    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty('Queue is empty!')
        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return item
    
    def enqueue(self, item):
        if len(self._data) == self._size:
            self._resize(len(self._data) * 2)
        index = (self._front + self._size) % len(self._data)
        self._data[index] = item
        self._size += 1
    