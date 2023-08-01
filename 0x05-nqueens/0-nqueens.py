#!/usr/bin/python3
'''N Queens Challenge'''

import sys

def is_safe(board, row, col):
  for i in range(row):
    if board[i][col] == 1:
      return False
  for i in range(row):
    for j in range(col):
      if board[i][j] == 1 and (row - i) == (col - j) or (row - i) == (j - col):
        return False
  return True

def solve_nqueens(board, row, n):
  if row == n:
    print(board)
    return
  for col in range(n):
    if is_safe(board, row, col):
      board[row][col] = 1
      solve_nqueens(board, row + 1, n)
      board[row][col] = 0

def main():
  if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number")
    sys.exit(1)
  if n < 4:
    print("N must be at least 4")
    sys.exit(1)
  board = [[0] * n for _ in range(n)]
  solve_nqueens(board, 0, n)

if __name__ == "__main__":
  main()

