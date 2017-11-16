#!/bin/python3
import sys
"""
# Description
# 
# Given a string, output its longest prefix which contains only digits.
#
# Example
#
# For inputString="123aa1", the output should be
# longestDigitsPrefix(inputString) = "123".
#
# Input/Output
#
# [input] string inputString
# Guaranteed constraints:
# 3 ≤ inputString.length ≤ 35.
# 
# [output] string
#
# Solution:
# Solution 1 is my original solution and is funtionally correct. Solution 2
# is a simpler solution using regex.
"""
##############
# SOLUTION 1 #
##############
def longestDigitsPrefix(inputString):
    prefix = []
    for char in inputString:
        if str.isdigit(char):
            prefix.append(char)
        else:
            break
    return ''.join(prefix)

##############
# SOLUTION 2 #
##############
#import re
#def longestDigitsPrefix(inputString):
#    return re.findall("^\\d*", inputString)[0]
	
print(longestDigitsPrefix("123aa1"))	                             # 123
print(longestDigitsPrefix("0123456789"))                           # 0123456789
print(longestDigitsPrefix("  3) always check for whitespaces"))    # 
print(longestDigitsPrefix("12abc34"))                              # 12
print(longestDigitsPrefix("the output is 42"))                     # 
