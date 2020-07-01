'''
Problem: Implement a doubly-linked list in Python
'''


class ListEmpty(Exception):
    pass


class DLinkedList:
    class _Node:
        def __init__(self, element, next, prev):
            self._element = element
            self._prev = prev
            self._next = next
        
        def get_element(self):
            return self._element
        
        def set_element(self, element):
            self._element = element
            
        def get_prev(self):
            return self._prev
        
        def set_prev(self, prev):
            self._prev = prev
            
        def get_next(self):
            return self._next
        
        def set_next(self, next):
            self._next = next
        
    def __init__(self):
        # Here we user header, and trailer sentinels
        self._header = DLinkedList._Node(None, None, None)
        self._trailer = DLinkedList._Node(None, None, None)
        self._header.set_next(self._trailer)
        self._trailer.set_prev(self._header)
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_first(self, element):
        node = DLinkedList._Node(element, next = self._header.get_next(), prev = self._header)
        self._header.get_next().set_prev(node)
        self._header.set_next(node)
        self._size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise ListEmpty('The list is empty!')
        
        node = self._header.get_next()
        self._header.set_next(node.get_next())
        node.get_next().set_prev(self._header)
        self._size -= 1
        return node.get_element()
    
    def add_last(self, element):
        node = DLinkedList._Node(element, next = self._trailer, prev = self._trailer.get_prev())
        self._trailer.get_prev().set_next(node)
        self._trailer.set_prev(node)
        self._size += 1
    
    def remove_last(self):
        node = self._trailer.get_prev()
        self._trailer.set_prev(node.get_prev())
        node.get_prev().set_next(self._trailer)
        self._size -= 1
        return node.get_element()
    
    
        
        
        
        
    
