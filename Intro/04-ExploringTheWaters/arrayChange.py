#!/bin/python3
import sys
"""
# Description
# 
# You are given an array of integers. On each move you are allowed to increase
# exactly one of its element by one. Find the minimal number of moves required
# to obtain a strictly increasing sequence from the input.
#
# Example:
# 
# For inputArray = [1, 1, 1], the output should be
# arrayChange(inputArray) = 3.
#
# Pass 1 = [1, 2, 1]
# Pass 2 = [1, 2, 2]
# Pass 3 = [1, 2, 3]
#
# Input Format
#
# array.integer inputArray
# Array of integers
#
# Constraints
# 3 ≤ inputArray.length ≤ 10**5
# -105 ≤ inputArray[i] ≤ 10**5
#
# Output Format 
#
# integer
# The minimal number of moves needed to obtain a strictly increasing sequence
# from inputArray.
# It's guaranteed that for the given test cases the answer always fits signed 
# 32-bit integer type.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def arrayChange(inputArray):
    diff, numMoves = 0, 0
    for i in range(len(inputArray) - 1):
        if inputArray[i+1] <= inputArray[i]:
            diff = abs(inputArray[i+1] - inputArray[i]) + 1
            inputArray[i+1] = inputArray[i+1] + diff
            numMoves += diff
    return(numMoves)
    
print(arrayChange([1,1,1]))                      # 3
print(arrayChange([-1000,0,-2,0]))               # 5
print(arrayChange([2,1,10,1]))                   # 12
print(arrayChange([2,3,3,5,5,5,4,12,12,10,15]))  # 13