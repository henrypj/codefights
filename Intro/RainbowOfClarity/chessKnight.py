#!/bin/python3
import sys
"""
# Description
# 
# Given a position of a knight on the standard chessboard, find the number of 
# different moves the knight can perform.
#
# The knight can move to a square that is two squares horizontally and one 
# square vertically, or two squares vertically and one square horizontally 
# away from it. The complete move therefore looks like the letter L. Check 
# out the image below to see all valid moves for a knight piece that is placed 
# on one of the central squares.
#
#   +---+---+---+---+---+---+---+---+
# 8 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 7 |   |   | X |   | X |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   | X |   |   |   | X |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   |   | K |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   | X |   |   |   | X |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 |   |   | X |   | X |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 1 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# Example
#
# For cell = "a1", the output should be
# chessKnight(cell) = 2.
#
#   +---+---+---+---+---+---+---+---+
# 8 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 7 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 |   | X |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   |   | X |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 1 | K |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# For cell = "c2", the output should be
# chessKnight(cell) = 6
#
#   +---+---+---+---+---+---+---+---+
# 8 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 7 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 6 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 5 |   |   |   |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 4 |   | X |   | X |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 3 | X |   |   |   | X |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 2 |   |   | K |   |   |   |   |   |
#   +---+---+---+---+---+---+---+---+
# 1 | X |   |   |   | X |   |   |   |
#   +---+---+---+---+---+---+---+---+
#     A   B   C   D   E   F   G   H 
#
# Input/Output
# [input] string cell
# String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.
#
# [output] integer
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def chessKnight(cell):
    possibleCells = []
    knightCol = cell[0]
    knightRow = cell[1]
    numMoves = 0
    # Possible Positions = NE, EN, ES, SE, SW, WS, WN, NW
    # Calc NE
    if int(knightRow) + 2 <= 8 and (ord(knightCol) + 1) <= 104:
        numMoves += 1
    if int(knightRow) + 1 <= 8 and (ord(knightCol) + 2) <= 104:
        numMoves += 1
    if int(knightRow) - 1 >= 1 and (ord(knightCol) + 2) <= 104:
        numMoves += 1
    if int(knightRow) - 2 >= 1 and (ord(knightCol) + 1) <= 104:
        numMoves += 1
    if int(knightRow) - 2 >= 1 and (ord(knightCol) - 1) >= 97:
        numMoves += 1
    if int(knightRow) - 1 >= 1 and (ord(knightCol) - 2) >= 97:
        numMoves += 1
    if int(knightRow) + 1 <= 8 and (ord(knightCol) - 2) >= 97:
        numMoves += 1
    if int(knightRow) + 2 <= 8 and (ord(knightCol) - 1) >= 97:
       numMoves += 1
    return numMoves

print(chessKnight("a1"))	                             # 2
print(chessKnight("c2"))	                             # 6
print(chessKnight("d4"))	                             # 8
print(chessKnight("g6"))	                             # 6
