#!/bin/python3
import sys
"""
# Description
# 
# In the popular Minesweeper game you have a board with some mines and those 
# cells that don't contain a mine have a number in it that indicates the total
# number of mines in the neighboring cells. Starting off with some arrangement
# of mines we want to create a Minesweeper game setup.
#
# Example:
# 
# For
#
# matrix = [[true, false, false],
#           [false, true, false],
#           [false, false, false]]
#
# the output should be 
# minesweeper(matrix) = [[1, 2, 1],
#                        [2, 1, 1],
#                        [1, 1, 1]]  
#
# Check out the image below for better understanding:
#
# +---+---+---+          +---+---+---+
# | 1 |   |   |          | 1 | 2 | 1 |
# +---+---+---+          +---+---+---+
# |   | 1 |   |   ===>   | 2 | 1 | 1 |
# +---+---+---+          +---+---+---+
# |   |   |   |          | 1 | 1 | 1 |
# +---+---+---+          +---+---+---+
#
# Input Format
#
# array.array.boolean matrix
# A non-empty rectangular matrix consisting of boolean values - true if the 
# corresponding cell contains a mine, false otherwise.
#
# Constraints
# 2 ≤ matrix.length ≤ 5,
# 2 ≤ matrix[0].length ≤ 5
#
# Output Format
#
# array.array.integer
# Rectangular matrix of the same size as matrix each cell of which contains an
# integer equal to the number of mines in the neighboring cells. Two cells are
# called neighboring if they share at least one corner.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def minesweeper(matrix):
    rowMax  = len(matrix)
    colMax  = len(matrix[0])
    mineMap = [[0] * (colMax) for i in range(rowMax)]
    for row in range(rowMax):
        for col in range(colMax):
            # Check every neighbor in matrix for true and sum them
            if matrix[row][col] == True:
                if col < colMax-1:
                    mineMap[row][col+1] += 1    
                if col > 0:
                    mineMap[row][col-1] += 1
                if row < rowMax-1:
                    mineMap[row+1][col] += 1
                if row > 0:
                    mineMap[row-1][col] += 1                    
                if row > 0 and col < colMax-1:
                    mineMap[row-1][col+1] += 1
                if row > 0 and col > 0:
                    mineMap[row-1][col-1] += 1
                if row < rowMax-1 and col < colMax-1:
                    mineMap[row+1][col+1] += 1
                if row < rowMax-1 and col > 0:
                    mineMap[row+1][col-1] += 1
    return(mineMap)
    
print(minesweeper([[True,False,False],         # [[1,2,1] 
                   [False,True,False],         #  [2,1,1]
                   [False,False,False]]))      #  [1,1,1]]
    
print(minesweeper([[False,False,False],        # [[0,0,0] 
                   [False,False,False]]))      #  [0,0,0]]

print(minesweeper([[True,False,False,True],    # [[0,2,2,1] 
                   [False,False,True,False],   #  [3,4,3,3]
                   [True,True,False,True]]))   #  [1,2,3,1]]
    
