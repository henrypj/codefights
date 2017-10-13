#!/bin/python3
import sys
"""
# Description
# 
# Given a string, replace each its character by the next one in the English 
# alphabet (z would be replaced by a).
#
# Example:
# 
# For inputString = "crazy", the output should be
# alphabeticShift(inputString) = "dsbaz"
#
# Input Format
#
# string inputString
# Non-empty string consisting of lowercase English characters.
#
# Constraints
# 1 ≤ inputString.length ≤ 10
#
# Output Format
#
# string
# The result string after replacing all of its characters.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def alphabeticShift(inputString):
    shiftedString = ""
    for i in range(len(inputString)):
        if inputString[i] == "z":
            shiftedString += chr(97)
        else:
            shiftedString += chr(ord(inputString[i]) + 1)
    return shiftedString

print(alphabeticShift("crazy"))                 # dsbaz
print(alphabeticShift("z"))                     # a

