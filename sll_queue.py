'''
Problem: Using a singly linked list implement queue ADT
'''


from singly_linked_list import SLinkedList


class QueueEmpty(Exception):
    pass


class SllQueue:
    def __init__(self):
        self._data = SLinkedList()
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._data.is_empty()
    
    def enqueue(self, item):
        self._data.add_to_tail(item)
        
    def dequeue(self):
        if self.is_empty():
            raise QueueEmpty('The queue is empty!')
        return self._data.remove_from_head()
    
    def first(self):
        if self.is_empty():
            raise QueueEmpty('The queue is empty!')
        return self._data.peek()