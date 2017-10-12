#!/bin/python3
import sys
"""
# Description
# 
# Ratiorg got statues of different sizes as a present from CodeMaster for his 
# birthday, each statue having an non-negative integer size. Since he likes to
# make things perfect, he wants to arrange them from smallest to largest so 
# that each statue will be bigger than the previous one exactly by 1. He may 
# need some additional statues to be able to accomplish that. Help him figure 
# out the minimum number of additional statues needed.
#
# Example:
# 
# For statues = [6, 2, 3, 8], the output should be
# makeArrayConsecutive2(statues) = 3.
#
# Ratiorg needs statues of sizes 4, 5 and 7.
#
# Input Format
#
# array.integer statues, An array of distinct non-negative integers.
# 1 ≤ statues.length ≤ 10
# 0 ≤ statues[i] ≤ 20
#
# Output Format 
#
# The minimal number of statues that need to be added to existing statues such
# that it contains every integer size from an interval [L, R] (for some L, R) 
# and no other sizes.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
def makeArrayConsecutive2(statues):
    statuesSorted = sorted(statues)
    numStatues = 0
    for i in range(len(statues)-1):
        if statuesSorted[i+1] - statuesSorted[i] != 1:
            numStatues += statuesSorted[i+1] - statuesSorted[i] - 1

    return(numStatues)
    
print(makeArrayConsecutive2([6,2,3,8]))