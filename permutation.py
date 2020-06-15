'''
Problem: Given a string S, print all permutations of S (without replacement).
'''


# Swap place of two characters in a string S, and return a new string
def swap(S, i, j):
    t = list(S)
    temp = t[i]
    t[i] = t[j]
    t[j] = temp
    return ''.join(t)


def permute(S, start=0):
    if (len(S) - 1) == start:
        print(S)
    for i in range(start, len(S)):
        swapped = swap(S, i, start)
        permute(swapped, start+1)
    

# permute("ABCD", 0)
