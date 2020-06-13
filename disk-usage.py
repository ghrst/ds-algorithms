'''
Problem: Given a path, calculate the cumulative disk-space used by all entries (files/folders) in that path recursively (in bytes).
'''


import os


def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        entries = os.listdir(path)
        for p in entries:
            new_path = os.path.join(path, p)
            total += disk_usage(new_path)
            print(new_path)
    return total