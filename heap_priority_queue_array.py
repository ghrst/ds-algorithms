'''
Problem: Use array representation of a heap to implement a priority queue
'''



from priority_queue_base import PriorityQueueBase
from list_queue import QueueEmpty

class HeapPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def _parent(self, j):
        return (j-1) // 2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        
    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)
            
    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            smaller_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    smaller_child = right
            if self._data[smaller_child] < self._data[j]:
                self._swap(smaller_child, j)
                self._downheap(smaller_child)
    
    def add(self, key, value):
        self._data.append(self._Item(key, value))
        self._upheap(self._data[len(self._data) - 1])
        
    def min(self):
        if self.is_empty():
            raise QueueEmpty('Priority queue is empty!')
        item = self._data[0]
        return (item.get_key(), item.get_value())
    
    def remove_min(self):
        if self.is_empty():
            raise QueueEmpty('Priority queue is empty!')
        self._swap(0, len(self._data) - 1)
        item = self._data.pop()
        self._downheap(0)
        return (item.get_key(), item.get_value())