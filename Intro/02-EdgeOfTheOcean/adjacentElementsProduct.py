#!/bin/python3
import sys
"""
# Description
# 
# Given an array of integers, find the pair of adjacent elements that has the 
# largest product and return that product.
#
# Example:
# 
# For inputArray = [3, 6, -2, -5, 7, 3], the output should be
# adjacentElementsProduct(inputArray) = 21.
#
# 7 and 3 produce the largest product.
#
# Input Format
#
# array.integer inputArray, An array of integers containing at least two elements
# 2 ≤ inputArray.length ≤ 10,
# -1000 ≤ inputArray[i] ≤ 1000.
#
# Output Format 
#
# The largest product of adjacent elements.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def adjacentElementsProduct(inputArray):
    for i in range(len(inputArray)-1):
        if i == 0:
            maxProduct = inputArray[i] * inputArray[i+1]
        if inputArray[i] * inputArray[i+1] > maxProduct:
            maxProduct = inputArray[i] * inputArray[i+1]

    return(maxProduct)

print(adjacentElementsProduct([3,6,-2,-5,7,3]))
print(adjacentElementsProduct([-23,4,-3,8,-12]))