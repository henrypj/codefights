#!/bin/python3
import sys
"""
# Description
# 
# Given an array of strings, return another array containing all of its longest
# strings.
#
# Example:
# 
# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
#
# Input Format
#
# array.string inputArray, A non-empty array.
# 1 ≤ inputArray.length ≤ 10,
# 1 ≤ inputArray[i].length ≤ 10.
#
# Output Format 
#
# Array of the longest strings, stored in the same order as in the inputArray.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def allLongestStrings(inputArray):
    L = []
    maxLen = 0
    for i in range(len(inputArray)):
        if len(inputArray[i]) == maxLen:
            L.append(inputArray[i])
        elif len(inputArray[i]) > maxLen:
            maxLen = len(inputArray[i])
            del L[:]
            L.append(inputArray[i])
    return L

A = ["aba", "aa", "ad", "vcd", "aba"]
print(allLongestStrings(A))