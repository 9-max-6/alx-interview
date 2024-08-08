#!/usr/bin/python3
""" module: minOperations
"""

def minOperations(n):
    if not isinstance(n, int) or n <= 0:
        return 0
    ops_count = 0
    clipboard = 0
    done = 1
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        elif (n - done) % done == 0:
            clipboard = done
            done += clipboard
            ops_count += 2
        else:
            done += clipboard
            ops_count += 1
    return ops_count
