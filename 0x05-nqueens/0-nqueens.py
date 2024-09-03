#!/usr/bin/python3
"""module: script - nqueens and backtracking"""
import sys


def get_exempt_row(point, queen_count):
    """A function that determines the coordinates in the row
    to be exempted from the solution
    point: format -> "ab" where a is a char 0-queen_count-1
    and b is a char 0-queen_count-1

    queen_count: size of the square
    """
    exempt_row = []
    for i in range(queen_count):
        fir_char = point[0]
        new_char = str(i)
        exempt_point = fir_char + new_char
        exempt_row.append(exempt_point)
    return exempt_row

def get_exempt_col(point, queen_count):
    """A function that determines the coordinates in the column
    to be exempted from the solution
    point: format -> "ab" where a is a char 0-queen_count-1
    and b is a char 0-queen_count-1

    queen_count: size of the square
    """
    exempt_col = []
    for i in range(queen_count):
        sec_char = point[1]
        new_char = str(i)
        exempt_point = new_char + sec_char
        exempt_col.append(exempt_point)
    return exempt_col

def get_exempt_diag_1(point, queen_count):
    """A function to determine which points
    to exempt in the leading diagonal
    """
    exempt_diag = []
    it = [int(char) for char in point]

    # positive
    for i in range(queen_count):
        new_first_char = it[0] + i
        new_second_char = it[1] + i
        if new_first_char < queen_count and new_second_char < queen_count:
            exempt_diag.append(str(new_first_char) + str(new_second_char))
        else:
            break

    # negative
    for j in range(1, queen_count):
        new_first_char = it[0] - j
        new_second_char = it[1] - j
        if new_first_char >= 0 and new_second_char >= 0:
            exempt_diag.append(str(new_first_char) + str(new_second_char))
        else:
            break
    
    return exempt_diag

def get_exempt_diag_2(point, queen_count):
    """A function to determine which points
    to exempt in a non-leading diagonal
    steps:
    1. Split the point into two characters
    2. Loop while less than queen_count in two directions
    3. Only add a point if the constraints for any of the point.
    """
    exempt = []
    it = [int(char) for char in point]

    # first char +
    # second char -
    for i in range(1, queen_count):
        new_first_char = it[0] + i
        new_second_char = it[1] - i
        if new_first_char < queen_count and new_second_char >= 0:
            exempt.append(str(new_first_char) + str(new_second_char))
        else:
            break
    
    # first char -
    # second char +
    for i in range(1, queen_count):
        new_first_char = it[0] - i
        new_second_char = it[1] + i
        if new_first_char >= 0 and new_second_char < queen_count:
            exempt.append(str(new_first_char) + str(new_second_char))
        else:
            break
    
    return exempt


def get_nqueens(queen_count):
    """
    Usage: nqueens N

    If the user called the program with the wrong
    number of arguments, print Usage: nqueens N,
    followed by a new line, and exit with the status 1

    where N must be an integer greater or equal to 4

    If N is not an integer, <print N must be a number>,
    followed by a new line, and exit with the status 1
    If N is smaller than 4, print <N must be at least 4>,
    followed by a new line, and exit with the status 1
    The program should print every possible solution to the problem

    One solution per line
    Format: see example
    You dont have to print the solutions in a specific order

    You are only allowed to import the sys module

    steps:
    1. Generate all the possible points
    2. Pick the first column first index
    3. Pick the next point in the next column

    Generate all the possible points and comprehend a list
    Place in the first column.
    Mark all the rows, columns, and diagonals as used
    Try a solution for the next column... 
    """
    if type(queen_count) is not int:
        print("N must be a number")
        sys.exit(1)

    if queen_count < 4:
        print("N must be at least 4")
        sys.exit(1)

    # get board
    solution_set = []
    exempted_set = []

    for i in range(queen_count):
        f_char = str(i)
        s_char = str(0)
        point = f_char + s_char
        new_solution_set = []
        new_solution_set.append(point)
        exempted_set.append(point)
        exempted_set.extend(get_exempt_col(point, queen_count))
        exempted_set.extend(get_exempt_row(point, queen_count))
        exempted_set.extend(get_exempt_diag_1(point, queen_count))
        exempted_set.extend(get_exempt_diag_2(point, queen_count))
        print(f"\n\nTrial Number {i}")

        for j in range(1, queen_count):
            second_char = str(j)
            for k in range(queen_count):
                first_char = str(k)
                nested_point = first_char + second_char
                if nested_point not in set(exempted_set):
                    print(f"Adding a new point: {nested_point}")
                    new_solution_set.append(nested_point)
                    exempted_set.append(nested_point)
                    exempted_set.extend(get_exempt_col(nested_point, queen_count))
                    exempted_set.extend(get_exempt_row(nested_point, queen_count))
                    exempted_set.extend(get_exempt_diag_1(nested_point, queen_count))
                    exempted_set.extend(get_exempt_diag_2(nested_point, queen_count))
                    break
                else:
                    print(f"Couldn't add: {nested_point}")
                    print(f"Current exempted set: {set(exempted_set)}")
        print(new_solution_set)
        solution_set.append(new_solution_set)
        new_solution_set.clear()
        exempted_set.clear()

    return solution_set
    

if __name__=='__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    else:
        print(get_nqueens(int(sys.argv[1])))
