#!/bin/python3
import sys
"""
# Description
# 
# Given two strings, find the number of common characters between them.
#
# Example:
# 
# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.
#
# Input Format
#
# string s1, A string consisting of lowercase latin letters a-z.
# 1 ≤ s1.length ≤ 15
#
# string s2, A string consisting of lowercase latin letters a-z.
# 1 ≤ s2.length ≤ 15
#
# Output Format 
#
# Integer
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def commonCharacterCount(s1, s2):
    commonCount = 0
    commonChars = list(set(s1) & set(s2))
    for i in range(len(commonChars)):
        numS1 = s1.count(commonChars[i])
        numS2 = s2.count(commonChars[i])
        commonCount += min(numS1, numS2)
    return commonCount
    
s1 = "aabcc"
s2 = "adcaa"
print(commonCharacterCount(s1, s2))