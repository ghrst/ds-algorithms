'''
Problem: Given an unordered sequence S, use insertion sort algorithm to sort it in increasing order. For more information about
insertion sort algorithm refer to: https://en.wikipedia.org/wiki/Insertion_sort
'''


def insertion_sort(S):
    for i in range(1, len(S)):
        cur = S[i]
        j = i
        while j > 0 and S[j - 1] > cur:
            S[j] = S[j-1]
            j -= 1
        S[j] = cur
      

    
