#!/bin/python3
import sys
"""
# Description
# 
# Given some integer, find the maximal number you can obtain by deleting 
# exactly one digit of the given number.
#
# Example
#
# For n = 152, the output should be
# deleteDigit(n) = 52;
#
# For n = 1001, the output should be
# deleteDigit(n) = 101.
#
# Input/Output
#
# [input] integer n
# Guaranteed constraints:
# 10 ≤ n ≤ 10**6.
#
# [output] integer
# 
# Solution:
"""
##############
# SOLUTION 1 #
##############
def deleteDigit(n):
    maxNum = 0
    nStr = str(n)
    for i in range(len(nStr)):
        nStr = nStr[:i] + nStr[i+1:]
        if int(nStr) > maxNum:
            maxNum = int(nStr)
        nStr = str(n)
    return maxNum

print(deleteDigit(152))	                             # 52
print(deleteDigit(1001))                             # 101
print(deleteDigit(10))	                             # 1
print(deleteDigit(1110110))                          # 111110
print(deleteDigit(222250))                           # 22250
print(deleteDigit(21202))                            # 2202
print(deleteDigit(540309))                           # 54309
