'''
Problem: Using positional lists implement a sorted priority queue
'''


from positional_list import PositionalList
from priority_queue_base import PriorityQueueBase
from list_queue import QueueEmpty


class SortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._list = PositionalList()
        
    def __len__(self, ):
        return len(self._list)
    
    def add(self, key, value):
        item = self._Item(key, value)
        if self.is_empty():
            self._list.add_first(item)
            return
        current = self._list.first()
        while current is not None and current.get_element() < item:
            current = self._list.after(current)
        if current is None:
            self._list.add_last(item)
        else:
            self._list.add_before(current, item)
    
    def min(self):
        if self.is_empty():
            raise QueueEmpty('Priority queue is empty')
        item = self._list.first().get_element()
        return(item.get_key(), item.get_value())
    
    def remove_min(self):
        if self.is_empty():
            raise QueueEmpty('Priority queue is empty')
        item = self._list.delete(self._list.first())
        return(item.get_key(), item.get_value())