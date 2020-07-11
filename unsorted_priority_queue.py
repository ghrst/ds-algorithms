'''
Problem: Using positional lists implement an unsorted priority queue
'''



from positional_list import PositionalList
from priority_queue_base import PriorityQueueBase
from list_queue import QueueEmpty

class UnsortedPriorityQueue(PriorityQueueBase):
    def __init__(self):
        self._list = PositionalList()
        
    def __len__(self):
        return len(self._list)
    
    def add(self, key, value):
        item = self._Item(key, value)
        self._list.add_first(item)
        
    def _find_min(self):
        if self.is_empty():
            raise QueueEmpty('Priority queue is empty!')
        
        minimum = self._list.first()
        walk = self._list.after(minimum)
        while walk is not None:
            if walk.get_element() < minimum.get_element():
                minimum = walk
            walk = self._list.after(walk)
        
        return minimum
    
    def min(self):
        smallest = self._find_min().get_element()
        return (smallest.get_key(), smallest.get_value())
    
    def remove_min(self):
        smallest = self._find_min()
        item = self._list.delete(smallest)
        return(item.get_key(), item.get_value())