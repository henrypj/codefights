#!/bin/python3
import sys
"""
# Description
# 
# Given a sorted array of integers a, find an integer x from a such that the 
# value of:
#
# abs(a[0] - x) + abs(a[1] - x) + ... + abs(a[a.length - 1] - x)
#
# is the smallest possible (here abs denotes the absolute value).
# If there are several possible answers, output the smallest one.
#
# Example:
# 
# For a = [2, 4, 7], the output should be
# absoluteValuesSumMinimization(a) = 4.
#
# Input Format
#
# array.integer a
# A non-empty array of integers, sorted in ascending order.
# 1 ≤ a.length ≤ 200
# -10**6 ≤ a[i] ≤ 10**6
#
# Output Format
#
# integer
#
# Solution:
# My solution 1 is a brute force attempt to implement what is described in
# the description above. However, what is really being asked is to return
# the median of the supplied list. Solution 2 does this by using Python's 
# median function that is part of statistics, and Solution 3 does this 
# with a simple calculation. 
"""
##############
# SOLUTION 1 #
##############
def absoluteValuesSumMinimization(a):
    for i in range(len(a)):
        print("i => ", i)
        print("x => ", a[i])
        prevValue = currValue if i > 0 else 99999999
        print("prevValue => ", prevValue)
        currValue = 0
        for j in range(len(a)):
            currValue += abs(a[j] - a[i])
        print("currValue => ", currValue)
        if currValue < prevValue:
            numLows = 0
        elif currValue == prevValue:
            numLows += 1
            if numLows == 1:
                lowVal = a[i]
        elif currValue > prevValue:
            return lowVal if numLows > 0 else a[i-1]

    return a[0]

##############
# SOLUTION 2 #
##############
#def absoluteValuesSumMinimization(a):
#    import statistics
#    return statistics.median_low(a)

##############
# SOLUTION 3 #
##############
#def absoluteValuesSumMinimization(a):
#    return a[(len(a)-1)//2]

    
print(absoluteValuesSumMinimization([2,4,7]))            # 4
print(absoluteValuesSumMinimization([1,1,3,4]))          # 1
print(absoluteValuesSumMinimization([23]))               # 23
print(absoluteValuesSumMinimization([-10, -10, -10, -10, -10, -9, -9, -9, -8, -8, -7, -6, -5, -4, -3, -2, -1, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]))            # 15
print(absoluteValuesSumMinimization([-4,-1]))            # -4
print(absoluteValuesSumMinimization([0,7,9]))            # 7
print(absoluteValuesSumMinimization([-1000000, -10000, -10000, -1000, -100, -10, -1, 0, 1, 10, 100, 1000, 10000, 100000, 1000000]))            # 0
print(absoluteValuesSumMinimization([1,2,3,5]))          # 2

























