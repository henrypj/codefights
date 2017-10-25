#!/bin/python3
import sys
"""
# Description
# 
# Check if the given string is a correct time representation of the 24-hour 
# clock.
#
# Example
#
# For time = "13:58", the output should be
# validTime(time) = true;
#
# For time = "25:51", the output should be
# validTime(time) = false;
#
# For time = "02:76", the output should be
# validTime(time) = false.
#
# Input/Output
#
# [input] string time
# A string representing time in HH:MM format. It is guaranteed that the first 
# two characters, as well as the last two characters, are digits.
#
# [output] boolean
# true if the given representation is correct, false otherwise.
#
# Solution:
"""
##############
# SOLUTION 1 #
##############
import re
def validTime(time):
#    return True if re.match('^([0-1][0-9]|[2][0-3]):([0-5][0-9])$', time) else False
    h,m=map(int,time.split(":"))
    return 0<=h<24 and 0<=m<60

print(validTime("13:58"))                # True
print(validTime("25:51"))                # False
print(validTime("02:76"))                # False
print(validTime("24:00"))                # False
