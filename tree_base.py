'''
Problem: Implement an abstract base class for tree ADT
'''


# Abstract base class
class Tree:
    class Position:
        def element(self):
            raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
        
        def __eq__(self, other):
            raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
        
        def __ne__(self, other):
            return not (self == other)
    
    def root(self):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def parent(self, p):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def num_children(self, p):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def children(self, p):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def __len__(self):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def is_root(self, p):
        return p == self.root()
    
    def is_leaf(self, p):
        return self.num_children(p) == 0
    
    def is_empty(self):
        return len(self) == 0
    
    def depth(self, p):
        if self.is_root(p):
            return 0
        return 1 + self.depth(self.parent(p))
    
    def height(self, p):
        if self.is_leaf(p):
            return 0
        return 1 + max(self.height(c) for c in self.children(p))
