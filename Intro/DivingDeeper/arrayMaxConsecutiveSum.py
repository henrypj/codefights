#!/bin/python3
import sys
"""
# Description
# 
# Given array of integers, find the maximal possible sum of some of its k 
# consecutive elements.
#
# Example:
# 
# For inputArray = [2, 3, 5, 1, 6] and k = 2, the output should be
# arrayMaxConsecutiveSum(inputArray, k) = 8.
#
# All possible sums of 2 consecutive elements are:
#    2 + 3 = 5
#    3 + 5 = 8
#    5 + 1 = 6
#    1 + 6 = 7
# Thus, the answer is 8.
#
# Input Format
#
# array.integer inputArray
# Array of positive integers.
# 3 ≤ inputArray.length ≤ 10**5
# 1 ≤ inputArray[i] ≤ 1000
#
# integer k
# An integer (not greater than the length of inputArray).
# 1 ≤ k ≤ inputArray.length
#
# Output Format
#
# integer
# The maximal possible sum.
#
# Solution:
# Solution 1 is functionally correct but timed out on test 7. The issue is that
# with large datasets, we are continually summing very large numbers (i.e. if
# say k is a very large value like 10000), when there is no need to do so. 
# Solution 2 sums the first k elements, then subsequent sums are obtained
# by adding the new number and subtracting the old.
"""
##############
# SOLUTION 1 #
##############
#def arrayMaxConsecutiveSum(inputArray, k):
#    numPairs = len(inputArray) - k + 1
#    if k == 1:
#        return max(inputArray)
#    else:
#        maxSum = 0
#        for i in range(numPairs):
#            pairSum = sum(inputArray[i:i+k])
#            if pairSum > maxSum:
#                maxSum = pairSum
#        return maxSum

##############
# SOLUTION 2 #
##############
def arrayMaxConsecutiveSum(inputArray, k):
    numPairs = len(inputArray) - k + 1
    if k == 1:
        return max(inputArray)
    else:
        prevSum = sum(inputArray[0:k])
        maxSum = prevSum
        for i in range(1,numPairs):
            pairSum = prevSum - inputArray[i-1] + inputArray[i+k-1]
            if pairSum > maxSum:
                maxSum = pairSum
            prevSum = pairSum
        return maxSum
    
print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))         # 8
print(arrayMaxConsecutiveSum([2, 4, 10, 1], 2))           # 14
print(arrayMaxConsecutiveSum([1, 3, 2, 4], 3))            # 9
print(arrayMaxConsecutiveSum([3, 2, 1, 1], 1))            # 3























