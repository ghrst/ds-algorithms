'''
Problem: We have a sequence called numbers. We want to calculate another sequence, called avg using numbers; such that avg[j] is the average
of the first j elements of numbers.
'''

# Quadratic solution
def prefix_avg_quadratic(numbers):
    n = len(numbers)
    avg = [0] * n
    for i in range(n):
        total = 0
        for j in range(i+1):
            total += numbers[j]
        avg[i] = total/(i+1)
    return avg


# Linear solution
def prefix_avg_linear(numbers):
    n = len(numbers)
    avg = [0] * n
    total = 0
    for i in range(n):
        total += numbers[i]
        avg[i] = total/(i + 1)
    return avg


if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9]
    print(prefix_avg_quadratic(numbers))
    print(prefix_avg_linear(numbers))
