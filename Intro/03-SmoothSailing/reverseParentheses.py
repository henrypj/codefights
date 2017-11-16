#!/bin/python3
import sys
"""
# Description
# 
# You have a string s that consists of English letters, punctuation marks, 
# whitespace characters, and brackets. It is guaranteed that the parentheses 
# in s form a regular bracket sequence.
#
# Your task is to reverse the strings contained in each pair of matching 
# parentheses, starting from the innermost pair. The results string should not 
# contain any parentheses.
#
# Example:
# 
# For string s = "a(bc)de", the output should be
# reverseParentheses(s) = "acbde".
#
# Input Format
#
# string s
# A string consisting of English letters, punctuation marks, whitespace 
# characters and brackets. It is guaranteed that parentheses form a regular 
# bracket sequence.
#
# Constraints
# 5 ≤ s.length ≤ 55
#
# Output Format 
#
# string
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def reverseParentheses(s):
    sequence = [[] for i in range(s.count("(")+1)]
    seqNum = 0
    for i in range(len(s)):
        if s[i] == "(":
            # At start of a sequence, so bump the seqNum
            seqNum += 1
        elif s[i] == ")":
            # At end of a sequence, extend sequence one level below with 
            # reversed sequence, then decrement the seqNum
            sequence[seqNum-1].extend(sequence[seqNum][::-1])
            sequence[seqNum] = []
            seqNum -= 1
        elif seqNum > 0:
            # Currently in a sequence, so just extend it
            sequence[seqNum].extend(s[i])
        else:
            # Not currently in a sequence, so append to sequence 0
            sequence[0].append(s[i])
    # Return sequence 0 as a string
    return(''.join(sequence[0]))
    
print(reverseParentheses("abc(de)f"))                 # acbde
print(reverseParentheses("a(bc)de"))                 # acbde
print(reverseParentheses("a(bcdefghijkl(mno)p)q"))   # apmnolkjihgfedcbq
