'''
Problem: Given an unordered sequence S, and selection sort algorithm return a sorted list. For more information about selection sort
refer to: https://en.wikipedia.org/wiki/Selection_sort
'''


def find_min(S, start):
    smallest = start
    for i in range(start + 1, len(S)):
        if S[smallest] > S[i]:
            smallest = i
    return smallest


def selection_sort(S, copy = True):
    # To prevent changing the original list
    if copy:
        S = S.copy()
    start = 0
    for i in range(len(S) - 1):
        smallest = find_min(S, start)
        S[start], S[smallest] = S[smallest], S[start]
        start += 1
    return S

    
