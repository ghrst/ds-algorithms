'''
Problem: Using a linked structure provide an implementation for a binary tree
'''


from binary_tree_base import BinaryTree

class LinkedBinaryTree(BinaryTree):
    class _Node:
        def __init__(self, item = None, parent = None, left = None, right = None):
            self._parent = parent
            self._left = left
            self._right = right
            self._data = item
            
        def get_data(self):
            return self._data
        
        def set_data(self, item):
            self._data = item
            
        def get_parent(self):
            return self._parent
        
        def set_parent(self, parent):
            self._parent = parent
            
        def get_left(self):
            return self._left
        
        def set_left(self, left):
            self._left = left
            
        def get_right(self):
            return self._right
        
        def set_right(self, right):
            self._right = right
        
    class _Position(BinaryTree._Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node
            
        def __eq__(self, other):
            return type(other) is type(self) and self._node is other._node
            
        def element(self):
            return self._node.get_data()
        
    def __init__(self):
        self._size = 0
        self._root = None
        
    def _make_position(self, node):
        if node is None:
            return None
        return self._Position(self, node)
    
    def _validate(self, p):
        if not isinstance(p, self._Position):
            raise TypeError('p must be of type LinkedBinaryTree._Position')
        if p._container is not self:
            raise ValueError('p does not belong to this binary tree')
        if p._node.get_parent() is p._node:
            raise ValueError('p is not valid!')
        return p._node
    
    def __len__(self):
        return self._size
    
    def root(self):
        return self._make_position(self._root)
    
    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node.get_parent())
    
    def left(self, p):
        node = self._validate(p)
        return self._make_position(node.get_left())
    
    def right(self, p):
        node = self._validate(p)
        return self._make_position(node.get_right())
    
    def num_children(self, p):
        node = self._validate(p)
        cnt = 0
        if node.get_left() is not None:
            cnt += 1
        if node.get_right() is not None:
            cnt += 1
        return cnt
    
    def add_root(self, item):
        if self._root is not None:
            raise ValueError('root exists!')
        self._size = 1
        self._root = self._Node(item = item)
        return self._make_position(self._root)
    
    def add_left(self, p, item):
        node = self._validate(p)
        if node.get_left() is not None:
            raise ValueError('Left child already exists. Use replace method.')
        node.set_left(self._Node(item, parent = node))
        self._size += 1
        return self._make_position(node.get_left())
    
    def add_right(self, p, item):
        node = self._validate(p)
        if node.get_right() is not None:
            raise ValueError('Right child already exists. Use replace method.')
        node.set_right(self._Node(item, parent = node))
        self._size += 1
        return self._make_position(node.get_right())
    
    def replace(self, p, item):
        node = self._validate(p)
        old = node.get_element()
        node.set_element(e)
        return old
    
    def delete(self, p):
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('This position has two children, we can not remove it!')
        if node.get_left():
            child = node.get_left()
        else:
            child = node.get_right()
            
        if child is not None:
            child.set_parent(node.get_parent())
        
        if node is self._root:
            self._root = child
        else:
            parent = node.get_parent()
            if node is parent.get_left():
                parent.set_left(child)
            else:
                parent.set_right(child)
        self._size -= 1
        node.set_parent(node)
        return node.get_data()
    
    def attach(self, p, tree1, tree2):
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('Position p must be a leaf!')
        if not type(self) is type(tree1) is type(tree2):
            raise TypeError('Trees are of different types!')
        self._size += len(tree1) + len(tree2)
        if not tree1.is_empty():
            tree1._root.set_parent(node)
            node.set_left(tree1._root)
            tree1._root = None
            tree1._size = 0
        if not tree2.is_empty():
            tree2._root.set_parent(node)
            node.set_left(tree2._root)
            tree2._root = None
            tree2._size = 0
            
        
        
            
        