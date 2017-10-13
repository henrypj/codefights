#!/bin/python3
import sys
"""
# Description
# 
# Given two cells on the standard chess board, determine whether they have 
# the same color or not.
#
# Example:
# 
# For cell1 = "A1" and cell2 = "C3", the output should be
# chessBoardCellColor(cell1, cell2) = true.
#
#   +---+---+---+---+---+---+---+---+
# 8 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 7 | D |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 5 | D |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 3 | D |   | X |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 1 | X |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
#     a   b   c   d   e   f   g   h
#
# For cell1 = "A1" and cell2 = "H3", the output should be
# chessBoardCellColor(cell1, cell2) = false.
#
#   +---+---+---+---+---+---+---+---+
# 8 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 7 | D |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 5 | D |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 3 | D |   | D |   | D |   | D | X |
#   +---+---+---+---+---+---+---+---+
# 2 |   | D |   | D |   | D |   | D |
#   +---+---+---+---+---+---+---+---+
# 1 | X |   | D |   | D |   | D |   |
#   +---+---+---+---+---+---+---+---+
#     a   b   c   d   e   f   g   h
#
# Input Format
#
# string cell1
#
# string cell2
#
#
# Output Format
#
# boolean
# true if both cells have the same color, false otherwise.
#
# Solution:
# Solution 1 simply checks to see if 
"""
##############
# SOLUTION 1 #
##############
def chessBoardCellColor(cell1, cell2):
    if ((cell1[0] in ["A","C","E","G"] and cell1[1] in ["1","3","5","7"]) or
        (cell1[0] in ["B","D","F","H"] and cell1[1] in ["2","4","6","8"])):
        if ((cell2[0] in ["A","C","E","G"] and cell2[1] in ["1","3","5","7"]) or
            (cell2[0] in ["B","D","F","H"] and cell2[1] in ["2","4","6","8"])):
            return True
        else:
            return False
    else:
        if ((cell2[0] in ["A","C","E","G"] and cell2[1] in ["1","3","5","7"]) or
            (cell2[0] in ["B","D","F","H"] and cell2[1] in ["2","4","6","8"])):
            return False
        else:
            return True


print(chessBoardCellColor("A1", "C3"))          # True
print(chessBoardCellColor("A1", "H3"))          # False
print(chessBoardCellColor("A1", "A2"))          # False
print(chessBoardCellColor("A1", "B2"))          # True
print(chessBoardCellColor("B3", "H8"))          # False
print(chessBoardCellColor("C3", "B5"))          # False

    