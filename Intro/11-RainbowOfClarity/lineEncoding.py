#!/bin/python3
import sys
"""
# Description
# 
# Given a string, return its encoding defined as follows:
#
# - First, the string is divided into the least possible number of disjoint 
#   substrings consisting of identical characters 
#   * for example, "aabbbc" is divided into ["aa", "bbb", "c"]
#
# - Next, each substring with length greater than one is replaced with a 
#   concatenation of its length and the repeating character 
#   * for example, substring "bbb" is replaced by "3b"
#
# - Finally, all the new strings are concatenated together in the same order 
#   and a new string is returned.
#
# Example
#
# For s = "aabbbc", the output should be
# lineEncoding(s) = "2a3bc"
#
# Input/Output
#
# [input] string s
# String consisting of lowercase English letters.
# Guaranteed constraints:
# 4 ≤ s.length ≤ 15.
#
# [output] string
# Encoded version of s.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def lineEncoding(s):
    prevChar = s[0]
    charCount = 0
    newLine = ""
    for char in s:
        print(char)
        if char == prevChar:
            charCount += 1
        else:
            if charCount == 1:
                newLine += prevChar
            else:
                newLine += str(charCount) + prevChar
            charCount = 1
            prevChar = char

    if charCount == 1:
        newLine += prevChar
    else:
        newLine += str(charCount) + prevChar
            
    return newLine

print(lineEncoding("aabbbc"))               # 2a3bc
print(lineEncoding("abbcabb"))              # a2bca2b
print(lineEncoding("abcd"))                 # abcd
