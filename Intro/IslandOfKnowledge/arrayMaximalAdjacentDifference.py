#!/bin/python3
import sys
"""
# Description
# 
# Given an array of integers, find the maximal absolute difference between any 
# two of its adjacent elements.
#
# Example:
# 
# For inputArray = [2, 4, 1, 0], the output should be
# arrayMaximalAdjacentDifference(inputArray) = 3.
#
# Input Format
#
# array.integer inputArray
#
# Constraints
# 3 ≤ inputArray.length ≤ 10
# -15 ≤ inputArray[i] ≤ 15
#
# integer
# The maximal absolute difference.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def arrayMaximalAdjacentDifference(inputArray):
    maxDiff = 0
    for i in range(len(inputArray) - 1):
        if abs(inputArray[i] - inputArray[i+1]) > maxDiff:
            maxDiff = abs(inputArray[i] - inputArray[i+1])
    return maxDiff
    
print(arrayMaximalAdjacentDifference([2,4,1,0]))        # 3
print(arrayMaximalAdjacentDifference([1,1,1,1]))        # 0
print(arrayMaximalAdjacentDifference([-1,4,10,3,-2]))   # 7