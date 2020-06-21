'''
Problem: Given a sequence of numbers S, use a recursive implementation to add them, and return the sum.
'''


def recursive_sum(S):
    if len(S) == 1:
        return S[0]
    return S[len(S) - 1] + recursive_sum(S[0:len(S) - 1])
