'''
Problem: We have three sequences of numbers A, B, and C. Assuming these sequences do not contain duplicate values; we want to know whether
intersection of these three sequences is empty or not?
'''

# Cubic solution
def disjoint_cubic(A, B, C):
    for a in A:
        for b in B:
            for c in C:
                if a == b == c:
                    return False
    return True


# Quadratic solution
def disjoint_quadratic(A, B, C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if b == c:
                        return False
    return True
        
    

            
        
    

