#x`x`!/bin/python3
import sys
"""
# Description
# 
# Construct a square matrix with a size N × N containing integers from 1 to 
# N * N in a spiral order, starting from top-left and in clockwise direction.
#
# Example
# 
# For n = 3, the output should be
# spiralNumbers(n) = [[1, 2, 3],
#                     [8, 9, 4],
#                     [7, 6, 5]]
#
# Input/Output
#
# [input] integer n
# Matrix size, a positive integer.
# Guaranteed constraints:
# 3 ≤ n ≤ 10.
#
# [output] array.array.integer
#
# Solution:
#          [1, 2, 3]
#  3 x 3   [8, 9, 4]  
#          [7, 6, 5]
#  
#          [ 1,  2 , 3, 4]
#  4 x 4   [12, 13, 14, 5]
#          [11, 16, 15, 6]
#          [10,  9,  8, 7]
#  
#          [ 1,  2 , 3,  4, 5]
#          [16, 17, 18, 19, 6]
#  5 x 5   [15, 24, 25, 20, 7]
#          [14, 23, 22, 21, 8]
#          [13, 12, 11, 10, 9]
#
# There is a pattern to the matrices. A 3 x 3 matrix has 5 paths (Row 0, Col 2,
# Row 2, Col 0, Row 1). A 4 x 4 matrix has 7 paths, a 5 x 5 matrix has 9 paths
# etc.
# 
# Path 1 is Left to Right (%4 == 1)
# Path 2 is Top to Bottom (%4 == 2)
# Path 3 is Right to Left (%4 == 3)
# Path 4 is Bottom to Top (%4 == 0)
#
# We know how many paths are needed to complete the matrix of a specific size
# by taking the matrix size and adding the same size less 1. So a matrix of
# size 6 x 6 would take 11 paths.
# 
# By using the number of paths and the path number, we can determine the 
# direction of how to populate the specific row or column by taking modulus
# of 4 on the path number. For path #9 for example, 9 % 4 == 1, so it is
# equivalent of Path 1 above, which is Left to Right.
# 
# Given this information, we should be able to calculate the values for the
# new matrix in a loop through the number of paths, as solution 1 does below.
"""
##############
# SOLUTION 1 #
##############
def spiralNumbers(n):
    matrix = [[0 for i in range(n)] for j in range(n)]
    numPaths = n + n - 1
    
    for path in range(1, numPaths + 1):
        if path % 4 == 1:       # Row Left to Right
            row = path // 4
            for col in range(n):
                if col == 0 and row == 0:
                    matrix[row][col] = 1
                elif matrix[row][col] == 0:
                    matrix[row][col] = matrix[row][col-1] + 1
        elif path % 4 == 2:     # Col Top to Bottom
            col = n - (path // 4 + 1)
            for row in range(1, n):
                if matrix[row][col] == 0:
                    matrix[row][col] = matrix[row-1][col] + 1
        elif path % 4 == 3:     # Row Right to Left
            row = n - (path // 4 + 1)
            for col in range(n-2, -1, -1):
                if matrix[row][col] == 0:
                    matrix[row][col] = matrix[row][col+1] + 1
        elif path % 4 == 0:     # Col Bottom to Top
            col = path // 4 - 1
            for row in range(n-2, 0, -1):
                if matrix[row][col] == 0:
                    matrix[row][col] = matrix[row+1][col] + 1
    return matrix



print(spiralNumbers(3)) # [[1, 2, 3],
#                          [8, 9, 4],
#                          [7, 6, 5]]

print(spiralNumbers(4)) # [[ 1,  2,  3, 4],
#                          [12, 13, 14, 5],
#                          [11, 16, 15, 6],
#                          [10,  9,  8, 7]]

print(spiralNumbers(5)) # [[1, 2, 3, 4, 5],
#                          [16, 17, 18, 19, 6],
#                          [15, 24, 25, 20, 7],
#                          [14, 23, 22, 21, 8],
#                          [13, 12, 11, 10, 9]]