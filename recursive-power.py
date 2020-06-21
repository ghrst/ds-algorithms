'''
Problem: Assuming that the exponent K is always a non-negative integer, write a recursive function POWER(X, K) which raises the real value X to the K-th power
'''


# O(n)
def power(x, k):
    if k == 0:
        return 1
    return x * power(x, k-1)


# O(log(n))
def power2(x, k):
    if k == 0:
        return 1
    partial = power(x, k//2)
    result = partial * partial
    if k % 2 == 1:
        result *= x
    return result