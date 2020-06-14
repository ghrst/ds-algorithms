'''
Problem: Provide a recursive implementation for Tower of Hanoi problem. For a detailed problem statement refer to:
    https://en.wikipedia.org/wiki/Tower_of_Hanoi
'''


def move_tower(n, start, finish, temp):
    """
    n: this is the number of disks, and must be an integer
    start: Starting tower and must be a character. For example 'A'
    finish: Where the disks should be put (final tower)? A character like 'C'
    temp: The tower that we use as a temporary destination for moving disks. It must be a character like 'B'
    """
    if n == 1:
        print(start, "to", finish)
        return
    move_tower(n - 1, start, temp, finish)
    print(start, "to", finish)
    move_tower(n - 1, temp, finish, start)
    

# move_tower(6, 'A', 'C', 'B')
