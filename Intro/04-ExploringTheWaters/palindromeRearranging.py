#!/bin/python3
import sys
"""
# Description
# 
# Given a string, find out if its characters can be rearranged to form a palindrome.
#
# Example:
# 
# For inputString = "aabb", the output should be
# palindromeRearranging(inputString) = true.
#
# We can rearrange "aabb" to make "abba", which is a palindrome.
#
# Input Format
#
# string inputString
# A string consisting of lowercase English letters.
#
# Constraints
# 1 ≤ inputString.length ≤ 50.
#
# Output Format 
#
# boolean
# true if the characters of the inputString can be rearranged to form a 
# palindrome, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def palindromeRearranging(inputString):
    uniqChars = set(inputString)
    if len(inputString) % 2 == 0:        # Even num of chars
        numOdd = 0
        for char in uniqChars:
            if inputString.count(char) % 2 != 0:
                numOdd += 1
        return True if numOdd <= 1 else False
    else:                                # Odd num of chars
        if len(uniqChars) == 1:
            return True
        else:
            numOdd = 0
            for char in uniqChars:
                if inputString.count(char) % 2 != 0:
                    numOdd += 1
            return True if numOdd == 1 else False
            

print(palindromeRearranging("aabb"))                                # True
print(palindromeRearranging("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"))    # False
print(palindromeRearranging("abbcabb"))                             # True
print(palindromeRearranging("zyyzzzzz"))                            # True
print(palindromeRearranging("z"))                                   # True
print(palindromeRearranging("zaa"))                                 # True
print(palindromeRearranging("abca"))                                # False
