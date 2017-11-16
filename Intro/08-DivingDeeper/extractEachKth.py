#!/bin/python3
import sys
"""
# Description
# 
# Given array of integers, remove each kth element from it.
#
# Example:
# 
# For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output 
# should be:
# extractEachKth(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].
#
# Input Format
#
# array.integer inputArray
# 5 ≤ inputArray.length ≤ 15
# -20 ≤ inputArray[i] ≤ 20
#
# integer k
# 1 ≤ k ≤ 10
#
# Output Format
#
# array.integer
# inputArray without elements k - 1, 2k - 1, 3k - 1 etc.
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def extractEachKth(inputArray, k):
    outputArray = []
    for i in range(len(inputArray)):
        if (i+1)%k != 0:
            outputArray.append(inputArray[i])
    return outputArray
    
print(extractEachKth([1,2,3,4,5,6,7,8,9,10],3))         # [1,2,4,5,7,8,10]
print(extractEachKth([1,1,1,1,1],1))                    # []
print(extractEachKth([1,2,1,2,1,2,1,2],2))              # [1,1,1,1]























