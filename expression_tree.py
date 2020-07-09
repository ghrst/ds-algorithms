'''
Problem: Implement a binary tree which can be used to represent an arithmetic expression, and evaluate the expression
'''


from linked_binary_tree import BinaryTree

class ExpressionTree(BinaryTree):
    def __init__(self, token, left = None, right = None):
        super().__init__()
        if not isinstance(token, str):
            raise TypeError('token parameter must be a string!')
        
        self.add_root(token)
        if left is not None:
            if token not in '+*-/':
                raise ValueError('You must provide a valid operator. Valid operators are +, -, *, /')
            self.attach(self.root(), left, right)
            
    def __str__(self):
        pieces = []
        self.paren_recur(self.root(), pieces)
        return ''.join(pieces)
    
    def paren_recur(self, p, result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self.paren_recur(self.left(p), result)
            result.append(p.element())
            self.paren_recur(self.right(p), result)
            result.append(')')
        
    def evaluate(self):
        return self._evaluate_recur(self.root())
    
    def _evaluate_recur(self, p):
        if self.is_leaf(p):
            return float(p.element())
        operator = p.element()
        left_value = self._evaluate_recur(self.left(p))
        right_value = self._evaluate_recur(self.right(p))
        if operator == '+':
            return left_value + right_value
        elif operator == '-':
            return left_value - right_value
        elif operator == '*':
            return left_value * right_value
        else:
            return left_value / right_value