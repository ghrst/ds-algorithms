'''
Problem: Use a singly linked list to implement a stack ADT.
'''


from singly_linked_list import SLinkedList

class StackEmpty(Exception):
    pass


class SllStack:
    def __init__(self):
        self._data = SLinkedList()
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return self._data.is_empty()
    
    def push(self, item):
        self._data.add_to_head(item)
        
    def pop(self):
        if self._data.is_empty():
            raise StackEmpty('Stack is empty!')
        return self._data.remove_from_head()
    
    def top(self):
        if self._data.is_empty():
            raise StackEmpty('Stack is empty!')
        return self._data.peek()
    
    
