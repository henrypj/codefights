#!/bin/python3
import sys
"""
# Description
# Difficulty: Easy
# 
# Given the string, check if it is a palindrome.
#
# Example:
# 
# For inputString = "aabaa", the output should be
# checkPalindrome(inputString) = true;
#
# For inputString = "abac", the output should be
# checkPalindrome(inputString) = false;
#
# For inputString = "a", the output should be
# checkPalindrome(inputString) = true.
#
# Input Format
#
# string inputString, A non-empty string consisting of lowercase characters.
# 1 ≤ inputString.length ≤ 105
#
# Output Format 
#
# true if inputString is a palindrome, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def checkPalindrome(inputString):
    if inputString.lower() == inputString.lower()[::-1]:
        return True
    else:
        return False

print(checkPalindrome("aaabaaa"))
print(checkPalindrome("Arewenotdrawnonwardwefewdrawnonwardtonewera"))