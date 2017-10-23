#!/bin/python3
import sys
"""
# Description
# 
# Define a word as a sequence of consecutive English letters. Find the longest
# word from the given string.
#
# Example
#
# For text = "Ready, steady, go!", the output should be
# longestWord(text) = "steady".
#
# Input/Output
#
# [input] string text
# Guaranteed constraints:
# 4 ≤ text.length ≤ 50.
#
# [output] string
# The longest word from text. It's guaranteed that there is a unique output.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import re
def longestWord(text):
    wordList = re.findall('[a-zA-Z]{1,}', text)
    #maxLen = max(len(word) for word in wordList)
    #maxLenWordList = [x for x in wordList if len(x) == maxLen]
    return max(wordList, key=len) 

print(longestWord("Ready, steady, go!"))                # steady
print(longestWord("Ready[[[, steady, go!"))             # steady
print(longestWord("ABCd"))                              # ABCd
print(longestWord("A!! AA[]z[BB"))                         # AA
