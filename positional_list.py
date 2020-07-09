'''
Problem: Implement positional list ADT
'''


from doubly_linked_list import DLinkedList

class PositionalList(DLinkedList):
    class _Position:            
        def __init__(self, container, node):
            # Users do not use this constructor
            self._container = container
            self._node = node
            
        def get_element(self):
            return self._node.get_element()
        
        # Comparing positions
        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
                
        def __ne__(self, other):
            return not (self == other)
        
    def _validate(self, p):
        if not isinstance(p, self._Position):
            raise TypeError('p must be of type Position')
        if p._container is not self:
            raise ValueError('p does not belong to this list')
        if p._node.get_next() is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self, node):
        if node is self._header or node is self._trailer:
            return None
        else:
            return self._Position(self, node)
    
    def first(self):
        return self._make_position(self._header.get_next())
    
    def last(self):
        return self._make_position(self._trailer.get_prev())
    
    def before(self, p):
        node = self._validate(p)
        return self._make_position(node.get_prev())
    
    def after(self, p):
        node = self._validate(p)
        return self._make_position(node.get_next())
    
    def __iter__(self):
        cur = self.first()
        while cur is not None:
            yield cur.get_element()
            cur = self.after(cur)
            
    def _insert_between(self, element, prev, next):
        node = self._Node(element, next, prev)
        next.set_prev(node)
        prev.set_next(node)
        self._size += 1
        return self._make_position(node)
    
    def add_first(self, element):
        return self._insert_between(element, self._header, self._header.get_next())
    
    def add_last(self, element):
        return self._insert_between(element, self._trailer.get_prev(), self._trailer)
    
    def add_before(self, position, element):
        node = self._validate(position)
        return self._insert_between(element, node.get_prev(), node)
    
    def add_after(self, position, element):
        node = self._validate(position)
        return self._insert_between(element, node, node.get_next())
    
    def delete(self, position):
        node = self._validate(position)
        node.get_prev().set_next(node.get_next())
        node.get_next().set_prev(node.get_prev())
        self._size -= 1
        return node.get_element()
    
    def replace(self, position, element):
        node = self._validate(position)
        old = node.get_element()
        node.set_element(element)
        return old