#!/bin/python3
import sys
"""
# Description
# 
# A string is said to be beautiful if b occurs in it no more times than a; 
# c occurs in it no more times than b; etc.
#
# Given a string, check whether it is beautiful.
#
# Example
#
# For inputString = "bbbaacdafe", the output should be
# isBeautifulString(inputString) = true;
#
# For inputString = "aabbb", the output should be
# isBeautifulString(inputString) = false;
#
# For inputString = "bbc", the output should be
# isBeautifulString(inputString) = false.
#
# Input/Output
#
# [input] string inputString
# A string of lowercase letters.
# Guaranteed constraints:
# 3 ≤ inputString.length ≤ 50.
#
# [output] boolean
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import string
def isBeautifulString(inputString):
    uniqueChars = set(inputString)
    prevCount = 51
    for char in string.ascii_lowercase:
        if inputString.count(char) > prevCount:
            return False
        prevCount = inputString.count(char)
    return True

#print(isBeautifulString("bbbaacdafe"))                         # True
#print(isBeautifulString("aabbb"))                              # False
#print(isBeautifulString("bbc"))                                # False
#print(isBeautifulString("bbbaa"))                              # False
#print(isBeautifulString("abcdefghijklmnopqrstuvwxyzz"))        # False
#print(isBeautifulString("abcdefghijklmnopqrstuvwxyz"))         # True
#print(isBeautifulString("abcdefghijklmnopqrstuvwxyzqwertuiopasdfghjklxcvbnm")) # True
print(isBeautifulString("fyudhrygiuhdfeis"))                   # False
print(isBeautifulString("zaa"))                                # False
print(isBeautifulString("zyy"))                                # False
