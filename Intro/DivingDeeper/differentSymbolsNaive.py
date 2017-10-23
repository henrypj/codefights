#!/bin/python3
import sys
"""
# Description
# 
# Given a string, find the number of different characters in it.
#
# Example:
# 
# For s = "cabca", the output should be
# differentSymbolsNaive(s) = 3.
# There are 3 different characters a, b and c.
#
# Input Format
#
# string s
# A string of lowercase latin letters.
# 3 ≤ s.length ≤ 15.
#
# Output Format
#
# integer
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def differentSymbolsNaive(s):
    return len(set(s))
    
print(differentSymbolsNaive("caba"))         # 3
print(differentSymbolsNaive("aba"))          # 2























