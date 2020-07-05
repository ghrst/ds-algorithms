'''
Problem: Implement an abstract base class representing a binary tree
'''


from tree_base import Tree


class BinaryTree(Tree):
    def left(self, p):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def right(self, p):
        raise NotImplementedError('This method is not implemented yet! Implement it in a subclass.')
    
    def sibling(self, p):
        if self.is_root(p):
            return None
        parent = self.parent(p)
        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)
        
    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
