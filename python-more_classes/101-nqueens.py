#!/usr/bin/python3
"""This class is going to solve the n-Queen problems"""

import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
N = int(sys.argv[1])
if N < 4:
    print("N must be at least 4")
    sys.exit(1)


def isSafe(mat, row, col):
    """ Check this column in previous rows """
    for i in range(row):
        if mat[i][col]:
            return 0
    # check upper diagonal on left side
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if mat[i][j]:
            return 0
        i -= 1
        j -= 1
    # check upper diagonal on right side
    i, j = row - 1, col + 1
    while i >= 0 and j < len(mat):
        if mat[i][j]:
            return 0
        i -= 1
        j += 1
    return 1


def placeQueens(row, mat, result):
    """recursive function to place queens"""
    n = len(mat)
    # base case: all queens are placed
    if row == n:
        h_mat = []
        for i in range(n):  # row
            for j in range(n):  # col
                if mat[i][j]:
                    h_mat.append([i, j])  # Format as [row, col]
        result.append(h_mat)
        return
    else:
        for col in range(n):
            # Can queen be placed?
            if isSafe(mat, row, col):
                mat[row][col] = 1
                placeQueens(row + 1, mat, result)

                # backtrack
                mat[row][col] = 0


def nqueen(N):
    """function to find the nqueen solution"""
    mat = [[0] * N for _ in range(N)]  # initialization of the result matrix
    result = []
    # Place queens
    placeQueens(0, mat, result)
    for i in result:
        print(i)  # Prints the list format directly
    return result


nqueen(N)
