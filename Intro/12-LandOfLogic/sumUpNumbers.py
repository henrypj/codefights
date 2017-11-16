#!/bin/python3
import sys
"""
# Description
# 
# CodeMaster has just returned from shopping. He scanned the check of the 
# items he bought and gave the resulting string to Ratiorg to figure out the
# total number of purchased items. Since Ratiorg is a bot he is definitely 
# going to automate it, so he needs a program that sums up all the numbers 
# which appear in the given input.
#
# Help Ratiorg by writing a function that returns the sum of numbers that 
# appear in the given inputString.
#
# Example
#
# For inputString = "2 apples, 12 oranges", the output should be
# sumUpNumbers(inputString) = 14.
#
# Input/Output
#
# [input] string inputString
# Guaranteed constraints:
# 6 ≤ inputString.length ≤ 60.
# 
# [output] integer
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import re
def sumUpNumbers(inputString):
    numbers = re.findall('[0-9]+', inputString)
    return sum(int(x) for x in numbers)


print(sumUpNumbers("2 apples, 12 oranges"))                # 14
print(sumUpNumbers("123450"))                              # 123450
print(sumUpNumbers("Your payment method is invalid"))      # 0
print(sumUpNumbers("1$$2 a,3;s 4"))                        # 10
print(sumUpNumbers("2 apples, 12 oranges ()DF 9"))         # 23
print(sumUpNumbers("01a10"))                               # 11
