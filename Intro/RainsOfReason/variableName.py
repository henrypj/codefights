#!/bin/python3
import sys
"""
# Description
# 
# Correct variable names consist only of Latin letters, digits and underscores
# and they can't start with a digit.
#
# Check if the given string is a correct variable name.
#
# Example:
# 
# For name = "var_1__Int", the output should be
# variableName(name) = true;
#
# For name = "qq-q", the output should be
# variableName(name) = false;
#
# For name = "2w2", the output should be
# variableName(name) = false.
#
# Input Format
#
# string name
#
# Constraints
# 1 ≤ name.length ≤ 10
#
# Output Format
#
# boolean
# true if name is a correct variable name, false otherwise.
#
# Solution:
# My Solution 1 passed all of the sample test cases, but failed on one of
# the hidden test cases. All of the comments suggested using regex for
# this problem, which is what I did with Solution 2 that passes all test
# cases. Pythex.org is a good site for testing regex.
#
# In Python, this can also be accomplished in one line with:
# return name.isidentifier()
"""
##############
# SOLUTION 1 #
##############
#def variableName(name):
#    validFirstChar = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#    validDigits    = "0123456789_"
#    if name[0] not in validFirstChar:
#        return False
#    for i in range(len(name)):
#        if name[i] not in (validFirstChar + validDigits):
#            return False
#    return True

##############
# SOLUTION 2 #
##############
import re
def variableName(name):
    isMatch = re.match('^[a-z_A-Z][a-z_A-Z0-9]*$', name)
    return True if isMatch else False

print(variableName("var_1__Int"))               # True
print(variableName("qq-q"))                     # False
print(variableName("2w2"))                      # True
print(variableName(" variable"))                # False
print(variableName("va[riable0"))               # False
print(variableName("variable0"))                # True
print(variableName("a"))                        # True
