#!/usr/bin/python3
"""
A function to determine the island perimeter
"""
def island_perimeter(grid):
    """
    Calculates the perimeter of a single island in a grid,
    where the grid is represented by a 2D array of integers
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
