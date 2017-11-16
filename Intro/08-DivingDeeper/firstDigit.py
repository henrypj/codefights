#!/bin/python3
import sys
"""
# Description
# 
# Find the leftmost digit that occurs in a given string.
#
# Example:
# 
# For inputString = "var_1__Int", the output should be
# firstDigit(inputString) = '1';
#
# For inputString = "q2q-q", the output should be
# firstDigit(inputString) = '2';
#
# For inputString = "0ss", the output should be
# firstDigit(inputString) = '0'.
#
# Input Format
#
# string inputString
# 3 ≤ inputString.length ≤ 10.
#
# Output Format
#
# char
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def firstDigit(inputString):
    import re
    return re.search(r'\d+',inputString).group()[0]
    
print(firstDigit("var_1_Int"))         # 1
print(firstDigit("q2q-q"))             # 2
print(firstDigit("0ss"))               # 0
print(firstDigit("111"))               # 1























