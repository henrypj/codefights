#!/bin/python3
import sys
"""
# Description
# 
# Given a rectangular matrix containing only digits, calculate the number of 
# different 2 × 2 squares in it.
#
# Example
#
# For
# matrix = [[1, 2, 1],
#           [2, 2, 2],
#           [2, 2, 2],
#           [1, 2, 3],
#           [2, 2, 1]]
#
# the output should be
# differentSquares(matrix) = 6.
#
# Here are all 6 different 2 × 2 squares:
# 1 2
# 2 2
#
# 2 1
# 2 2
#
# 2 2
# 2 2
#
# 2 2
# 1 2
#
# 2 2
# 2 3
#
# 2 3
# 2 1
#
# Input/Output
#
# [input] array.array.integer matrix
# Guaranteed constraints:
# 1 ≤ matrix.length ≤ 100,
# 1 ≤ matrix[i].length ≤ 100,
# 0 ≤ matrix[i][j] ≤ 9.
#
# [output] integer
# The number of different 2 × 2 squares in matrix.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def differentSquares(matrix):
    squares = set()
    if len(matrix) < 2 or len(matrix[0]) < 2:
        return 0
    for row in range(len(matrix)-1):
        for col in range(len(matrix[0])-1):
            squares.add((matrix[row][col], matrix[row][col+1], matrix[row+1][col], matrix[row+1][col+1]))
    return len(squares)


print(differentSquares([[1,2,1], 
                        [2,2,2], 
                        [2,2,2], 
                        [1,2,3], 
                        [2,2,1]]))                # 6

print(differentSquares([[9,9,9,9,9], 
                        [9,9,9,9,9], 
                        [9,9,9,9,9], 
                        [9,9,9,9,9], 
                        [9,9,9,9,9], 
                        [9,9,9,9,9]]))            # 1

print(differentSquares([[3]]))                    # 0 
print(differentSquares([[3,4,5,6,7,8,9]]))        # 0 
print(differentSquares([[3], 
                        [4], 
                        [5], 
                        [6], 
                        [7]]))                    # 0 
print(differentSquares([[2,5,3,4,3,1,3,2], 
                        [4,5,4,1,2,4,1,3], 
                        [1,1,2,1,4,1,1,5], 
                        [1,3,4,2,3,4,2,4], 
                        [1,5,5,2,1,3,1,1], 
                        [1,2,3,3,5,1,2,4], 
                        [3,1,4,4,4,1,5,5], 
                        [5,1,3,3,1,5,3,5], 
                        [5,4,4,3,5,4,4,4]]))      # 54
print(differentSquares([[1,1,1,1,1,1,2,2,2,3,3,3,9,9,9,2,3,9]]))        # 0 
