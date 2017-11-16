#!/bin/python3
import sys
"""
# Description
# 
# Given the positions of a white bishop and a black pawn on the standard chess
# board, determine whether the bishop can capture the pawn in one move.
#
# The bishop has no restrictions in distance for each move, but is limited to 
# diagonal movement. Check out the example below to see how it can move:
#
#   +---+---+---+---+---+---+---+---+
# 8 |   |   |   |   |   |   |   | x |
#   +---+---+---+---+---+---+---+---+
# 7 | x |   |   |   |   |   | x |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   | x |   |   |   | x |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   | x |   | x |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   |   |   | B |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 |   |   | x |   | x |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   | x |   |   |   | x |   |   |
#   +---+---+---+---+---+---+---+---+
# 1 | x |   |   |   |   |   | x |   |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# Example
#
# For bishop = "a1" and pawn = "c3", the output should be
# bishopAndPawn(bishop, pawn) = true.
#
#   +---+---+---+---+---+---+---+---+
# 8 |   |   |   |   |   |   |   | x |
#   +---+---+---+---+---+---+---+---+
# 7 |   |   |   |   |   |   | x |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   |   |   |   |   | x |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   |   |   | x |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   |   |   | x |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 |   |   | P |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   | x |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 1 | B |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# For bishop = "h1" and pawn = "h3", the output should be
# bishopAndPawn(bishop, pawn) = false.
#
#   +---+---+---+---+---+---+---+---+
# 8 | x |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 7 |   | x |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   |   | x |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   |   | x |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   |   |   |   | x |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 |   |   |   |   |   | x |   | P |
#   +---+---+---+---+---+---+---+---+
# 2 |   |   |   |   |   |   | x |   |
#   +---+---+---+---+---+---+---+---+
# 1 |   |   |   |   |   |   |   | B |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# Solution:
# My Solution 1 passes all test cases, however there are solutions that are
# much simpler.
"""
##############
# SOLUTION 1 #
##############
def bishopAndPawn(bishop, pawn):
    possibleCells = []
    bishopCol = bishop[0]
    bishopRow = bishop[1]
    rows = "12345678"
    cols = "abcdefgh"
    bishopColIdx = cols.find(bishopCol)
    colsLeft = cols[:bishopColIdx][::-1]
    colsRight = cols[bishopColIdx+1:]
    bishopRowIdx = rows.find(bishopRow)
    rowsDown = rows[:bishopRowIdx][::-1]
    rowsUp = rows[bishopRowIdx+1:]

    for i in range(min(len(colsLeft), len(rowsDown))):
        possibleCells.append(colsLeft[i] + rowsDown[i])
    for i in range(min(len(colsLeft), len(rowsUp))):
        possibleCells.append(colsLeft[i] + rowsUp[i])
    for i in range(min(len(colsRight),len(rowsUp))):
        possibleCells.append(colsRight[i] + rowsUp[i])
    for i in range(min(len(colsRight), len(rowsDown))):
        possibleCells.append(colsRight[i] + rowsDown[i])
    
    return True if pawn in possibleCells else False

print(bishopAndPawn("d4", "c3"))	                             # True
print(bishopAndPawn("a1", "c3"))	                             # True
print(bishopAndPawn("h1", "h3"))	                             # False
print(bishopAndPawn("a5", "c3"))	                             # True
print(bishopAndPawn("g1", "f3"))	                             # False
print(bishopAndPawn("e7", "d6"))	                             # True
print(bishopAndPawn("e7", "a3"))	                             # True
print(bishopAndPawn("e3", "a7"))	                             # True
print(bishopAndPawn("a1", "h8"))	                             # True
print(bishopAndPawn("a1", "h7"))	                             # False
print(bishopAndPawn("h1", "a8"))	                             # True
