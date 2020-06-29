'''
Problem: Implement a singly linked list in Python
'''


class ListEmpty(Exception):
    pass


class SLinkedList:
    # Each node of the list
    class _Node:
        def __init__(self, item):
            self._element = item
            self._next = None
        
        def get_element(self):
            return self._element
        
        def set_element(self, item):
            self._element = item
        
        def set_next(self, next):
            self._next = next
            
        def get_next(self):
            return self._next
    
    def __init__(self):
        self._head = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def add_to_head(self, item):
        new = SLinkedList._Node(item)
        new.set_next(self._head)
        self._head = new
        self._size += 1
        
    def is_empty(self):
        return self._size == 0
    
    def remove_from_head(self):
        if self.is_empty():
            raise ListEmpty('The list is empty!')
        node = self._head
        self._head = node.get_next()
        self._size -= 1
        return node.get_element()
    
    def peek(self):
        if self.is_empty():
            raise ListEmpty('The list is empty!')
        return self._head.get_element()
    
    
    
        
        
        
        
        
    
