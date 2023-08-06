#!/usr/bin/python3
"""
N Queens Solver - Solves the N Queens problem using backtracking.

The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. This program will find and print all possible solutions
to the N queens problem, given a specific integer N.

Usage:
    python3 0-nqueens.py N

    where N (int): The size of the chessboard and the number of queens to
    be placed.

Returns:
    None
"""
import sys


def is_safe(board, row, col, N):
    """
    This function checks whether placing a queen at the given position
    (row, col) on the board will not attack any other queens that are
    already placed on the board.

    Args:
        board (list[list[int]]): The chessboard represented as a 2D list
        with integers.
        row (int): The row of the position being checked.
        col (int): The column of the position being checked.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it is safe to place a queen at the given position,
        False otherwise.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N Queens problem and print all possible solutions.


    Args:
        N (int): The size of the chessboard and the number of queens to
        be placed.

    Returns:
        None
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []

    def backtrack(row):
        """
        Backtracking function to find solutions.

        This function uses a backtracking approach to explore all possible
        arrangements of queens on the board. When a valid solution is found
        (i.e., all N queens are placed on the board without attacking each
        other), it appends the solution to the solutions list.

        Args:
            row (int): The current row being considered for queen placement.

        Returns:
            None
        """
        if row == N:
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0

    backtrack(0)
    print_solutions(solutions)


def print_solutions(solutions):
    """
    Print all the solutions.

    This function prints all the solutions to the N Queens problem.

    Args:
        solutions (list[list[list[int]]]): A list containing all possible
        solutions.

    Returns:
        None
    """
    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 1:
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(args[0])
        if N < 4:
            print("N must be at least 4")
            exit(1)

        solve_nqueens(N)

    except ValueError:
        print("N must be a number")
        exit(1)
