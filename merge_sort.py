'''
Problem: implement the merge sort. For an explanation of algorithm, and implementation techniques refer to:
https://en.wikipedia.org/wiki/Merge_sort
'''


def merge_sort(S):
    if len(S) <= 1:
        return S
    high = []
    low = []
    mid = len(S) // 2
    low = merge_sort(S[0:mid])
    high = merge_sort(S[mid:])
    return merge(low, high)
        

# To Do: Write another version of merge that does not affect it's arguments
# Merging two sorted arrays 
def merge(first, second):
    # Caution: This function changes first, and second
    temp = []
    # While the lists are not empty
    while first and second:
        if first[0] <= second[0]:
            temp.append(first[0])
            first.pop(0)
        else:
            temp.append(second[0])
            second.pop(0)
    # Adding any leftovers
    while first:
        temp.append(first.pop(0))
    while second:
        temp.append(second.pop(0))
    return temp