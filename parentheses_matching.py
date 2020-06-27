'''
Problem: Given an expression involving parenthesis, brackets, and braces write an algorithm to detect if each all pairs match or no. Here
we can use list_stack.py which contains ListStack class
'''


import list_stack


def match(expr):
    left = '([{'
    right = ')]}'
    S = list_stack.ListStack()
    for c in expr:
        if c in left:
            S.push(c)
        if c in right:
            if S.is_empty():
                return False
            if right.index(c) != left.index(S.pop()):
                return False
    return S.is_empty()
    
