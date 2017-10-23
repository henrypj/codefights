#!/bin/python3
import sys
"""
# Description
# 
# Given a string, find the shortest possible string which can be achieved by 
# adding characters to the end of initial string to make it a palindrome.
#
# Example
#
# For st = "abcdc", the output should be
# buildPalindrome(st) = "abcdcba".
#
# Input/Output
#
# [input] string st
# A string consisting of lowercase latin letters.
# Guaranteed constraints:
# 3 ≤ st.length ≤ 10.
# 
# [output] string
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])

def buildPalindrome(st):
    if isPal(st):
        return st
    else:
        chars = ""
        for char in st:
            chars = char + chars
            if isPal(st + chars):
                return(st + chars)

print(buildPalindrome("abcdc"))                  # abcdcba
print(buildPalindrome("ababab"))                 # abababa
print(buildPalindrome("abba"))                   # 
print(buildPalindrome("abaa"))                   # abaaba
