'''
Problem: Given a number n, calculate it's factorial n * n-1 * n-2 * ... * 1. Notice that 0! = 1
'''


def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_iter(n):
    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact


    

