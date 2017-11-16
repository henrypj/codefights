#!/bin/python3
import sys
"""
# Description
# 
# You have deposited a specific amount of dollars into your bank account. Each
# year your balance increases at the same growth rate. Find out how long it 
# would take for your balance to pass a specific threshold with the assumption 
# that you don't make any additional deposits.
#
# Example:
# 
# For deposit = 100, rate = 20 and threshold = 170, the output should be
# depositProfit(deposit, rate, threshold) = 3.
#
# Each year the amount of money on your account increases by 20%. It means that
# throughout the years your balance would be:
#
# - year 0: 100;
# - year 1: 120;
# - year 2: 144;
# - year 3: 172,8.
#
# Thus, it will take 3 years for your balance to pass the threshold, which is 
# the answer.
#
# Input Format
#
# integer deposit
# The initial deposit as a positive integer.
# 1 ≤ deposit ≤ 100.
#
# integer rate
# The rate of increase. Each year the balance increases by the rate percent of
# the current sum.
# 1 ≤ rate ≤ 100.
# 
# integer threshold
# The target balance.
# deposit < threshold ≤ 200.
#
# Output Format
#
# integer
# The number of years it would take to hit the threshold.
#
# Solution:
# 
"""
##############
# SOLUTION 1 #
##############
def depositProfit(deposit, rate, threshold):
    thresholdMet = False
    years   = 0
    currBal = deposit
    while not thresholdMet:
        years += 1
        currBal *= 1 + rate/100
        print("currBal => ", currBal)
        thresholdMet = True if currBal >= threshold else False
    return years

print(depositProfit(100,20,170))            # 3
print(depositProfit(100,1,101))             # 1
print(depositProfit(1,100,64))              # 6

























