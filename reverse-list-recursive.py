'''
Problem: Given a list S, reverse it.
'''


def reverse(S, start, end):
    if start < end - 1:
        S[start], S[end] = S[end], S[start]
        reverse(S, start + 1, end - 1)
