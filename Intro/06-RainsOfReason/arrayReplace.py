#!/bin/python3
import sys
"""
# Description
# 
# Given an array of integers, replace all the occurrences of elemToReplace 
# with substitutionElem.
#
# Example:
# 
# For inputArray = [1, 2, 1], elemToReplace = 1 and substitutionElem = 3, the 
# output should be
# arrayReplace(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
#
# Input Format
#
# array.integer inputArray
#
# Constraints
# 2 ≤ inputArray.length ≤ 10
# 0 ≤ inputArray[i] ≤ 10
#
# integer elemToReplace
#
# Constraints
# 0 ≤ elemToReplace ≤ 10
#
# integer substitutionElem
#
# Constraints
# 0 ≤ substitutionElem ≤ 10
#
# Output Format
#
# array.integer
#
# Solution:
# Wow, my first ever one line Python solution
"""
##############
# SOLUTION 1 #
##############
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return([substitutionElem if item == elemToReplace else item for item in inputArray])
    
    
    
print(arrayReplace([1,2,1], 1, 3))          # [3,2,3]    
print(arrayReplace([1,2,3,4,5], 3, 0))      # [1,2,0,4,5]    
print(arrayReplace([1,1,1], 1, 10))         # [10,10,10]    
