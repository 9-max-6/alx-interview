#!/usr/bin/python3
"""
 function that returns a list of integers representing the
 Pascal's triangle of n
"""

def pascal_triangle(n):
    """algorithm"""

    if n <= 0:
        return []

    blaise = []
    for i in range(n):
        
        if (i == 0):
            blaise.append([1])
        elif (i == 1):
            blaise.append([1, 1])
        else:
            new_row = []
            prev_row = blaise[i - 1]
            for j in range(i  + 1):
                if j == 0:
                    new_row.append(1)
                elif j == i:
                    new_row.append(1)
                else:
                    new_row.append(prev_row[j] + prev_row[j - 1])
            blaise.append(new_row)
    return blaise