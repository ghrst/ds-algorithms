'''
Problem: Assuming that the exponent K is always a non-negative integer, write a recursive function POWER(X, K) which raises the real value X to the K-th power
'''


def power(x, k):
    if k == 0:
        return 1
    return x * power(x, k-1)
