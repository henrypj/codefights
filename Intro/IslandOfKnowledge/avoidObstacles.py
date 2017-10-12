#!/bin/python3
import sys
"""
# Description
# 
# You are given an array of integers representing coordinates of obstacles 
# situated on a straight line.
# 
# Assume that you are jumping from the point with coordinate 0 to the right. 
# You are allowed only to make jumps of the same length represented by some 
# integer.
#
# Find the minimal length of the jump enough to avoid all the obstacles.
#
# Example:
# 
# For inputArray = [5, 3, 6, 7, 9], the output should be
# avoidObstacles(inputArray) = 4.
#
# Check out the image below for better understanding:
#
#    +------------------+ +-----------------+ +-----------
#    |                  | |                 | |
# ---+----+----+----O----+----O----O----O----+----O----+----
#    0    1    2    3    4    5    6    7    8    9    10 
#
# Input Format
#
# array.Integer inputArray
# Non-empty array of positive integers.
#
# Constraints
# 2 ≤ inputArray.length ≤ 10,
# 1 ≤ inputArray[i] ≤ 40
#
# Output Format
#
# integer
# The desired length.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def avoidObstacles(inputArray):
    obstacles = sorted(inputArray)
    jumpDist = 2
    currPos  = 0
    minFound = False
    while not minFound and currPos <= 40:
        if currPos + jumpDist not in obstacles:
            currPos += jumpDist
        else:
            currPos   = 0
            jumpDist += 1
        if currPos > 40:
            minFound = True
    return jumpDist
        

print(avoidObstacles([5,3,6,7,9]))          # 4
print(avoidObstacles([2,3]))                # 4
print(avoidObstacles([1,4,10,6,2]))         # 7