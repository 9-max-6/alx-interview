#!/usr/bin/python3
"""module: script - nqueens and backtracking"""
import sys

solution_set = []

def get_board(queen_count):
    """a function to generate board"""
    board = []
    for i in range(queen_count):
        row = []
        for j in range(queen_count):
            row.append(str(i) + str(j))
        board.append(row)
    return board

def get_choices(point, board):
    """Gets choices for the current point"""
    row_number = int(point[1])
    choices = []

    for row in board:
        if row_number + 1 == len(board[0]):
            return []
        choices.append(row[row_number + 1])
    
    return choices


def get_exempt_row(point, queen_count):
    """A function that determines the coordinates in the row
    to be exempted from the solution
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

def get_exempt(point, queen_count):
    """A function to get all the exempt function for a point"""
    exempt = []
    exempt.extend(get_exempt_col(point, queen_count))
    exempt.extend(get_exempt_row(point, queen_count))
    exempt.extend(get_exempt_diag_1(point, queen_count))
    exempt.extend(get_exempt_diag_2(point, queen_count))

    return exempt

def find_solutions(point, board, queen_count, current_sol_set=[], exempted_set=set()):
    """Backtracking to find solutions"""
    if len(current_sol_set) == queen_count:
        solution_set.append(current_sol_set.copy())
        return

    choices = get_choices(point, board)
    for choice in choices:
        if choice not in exempted_set:
            current_sol_set.append(choice)
            new_exemptions = set(get_exempt(choice, queen_count))
            exempted_set.update(new_exemptions)
            
            find_solutions(choice, board, queen_count, current_sol_set, exempted_set)
            
            # Undo choices
            exempted_set.difference_update(new_exemptions)
            current_sol_set.pop()

def get_nqueens(queen_count):
    """Function to solve N-Queens using backtracking"""
    board = get_board(queen_count)
    for i in range(queen_count):
        find_solutions(board[i][0], board, queen_count)
    return solution_set

if __name__ == '__main__':
    arg_len = len(sys.argv)
    if arg_len != 2:
        print("Usage: nqueens N")
        print(get_nqueens(4))
    else:
        print(get_nqueens(int(sys.argv[1])))
