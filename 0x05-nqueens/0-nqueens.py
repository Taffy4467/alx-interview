#!/usr/bin/python3
'''N Queens Challenge'''

def checks(board, row, col):

    for i in range(col):
        if board[i] is row or abs(board[i] - row) is abs(i - col):
            return False
    return True


def cboard(board, col):

    size = len(board)
    if col is size:
        print(str([[i, board[i]] for i in range(size)]))
        return
    for n in range(size):
        if checks(board, n, col):
            board[col] = n
            cboard(board, col + 1)


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    n = 0
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [0 for col in range(n)]
    cboard(board, 0)
