'''
Problem: We are given a single sequence S, with n elements, and asked whether all elements of the collection are unique or not?
'''


# Quadratic solution
def unique_quadratic(S):
    n = len(S)
    for i in range(n):
        for j in range(i+1, n):
            if S[i] == S[j]:
                return False
    return True


# nlogn solution
def unique_nlogn(S):
    sorted_seq = sorted(S)
    for i in range(len(sorted_seq) - 1):
        if sorted_seq[i] == sorted_seq[i+1]:
            return False
    return True