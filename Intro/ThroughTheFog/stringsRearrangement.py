#!/bin/python3
import sys
"""
# Description
# 
# Given an array of equal-length strings, check if it is possible to rearrange 
# the strings in such a way that after the rearrangement the strings at 
# consecutive positions would differ by exactly one character.
#
# Example:
# 
# For inputArray = ["aba", "bbb", "bab"], the output should be
# stringsRearrangement(inputArray) = false;
#
# All rearrangements don't satisfy the description condition.
#
# For inputArray = ["ab", "bb", "aa"], the output should be
# stringsRearrangement(inputArray) = true.
#
# Strings can be rearranged in the following way: "aa", "ab", "bb".
#
# Input Format
#
# array.string inputArray
# A non-empty array of strings of lowercase letters.
# 2 ≤ inputArray.length ≤ 10
# 1 ≤ inputArray[i].length ≤ 15
#
# Output Format
#
# boolean
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def stringsRearrangement(inputArray):
    import itertools
    perms = list(itertools.permutations(inputArray))
    #for i in range(len(perms)):
    for perm in perms:
        for i in range(len(perms[0])-1):
            numDiffs = 0
            for j in range(len(perm[0])):
                if perm[i][j] != perm[i+1][j]:
                    numDiffs += 1
            if numDiffs == 0 or numDiffs > 1:
                break
        if numDiffs == 1:
            return True               
    return False
    
print(stringsRearrangement(["aba","bbb","bab"]))                    # False
print(stringsRearrangement(["ab","bb","aa"]))                       # True
print(stringsRearrangement(["q","q"]))                              # False
print(stringsRearrangement(["zzzzab","zzzzbb","zzzzaa"]))           # True
print(stringsRearrangement(["ab","ad","ef","eg"]))                  # False
print(stringsRearrangement(["abc","bef","bcc","bec","bbc","bdc"]))  # True
print(stringsRearrangement(["abc","abx","axx","abc"]))              # False
print(stringsRearrangement(["f","g","a","h"]))                      # True
print(stringsRearrangement(["aba","bbb","bab"]))                    # False
print(stringsRearrangement(["ca", "ba", "aa", "ab", "ac", "bb"]))   # True
























